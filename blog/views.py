from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
import markdown as md
from datetime import datetime
from django.urls import reverse
from django.db.models import Q

from blog.models import *

from .models import Reply
from . import mail

# Create your views here.


def index(request):
    if request.method == "POST":
        search_text = request.POST.get("search")
        if search_text is not None and search_text != "":
            print("redirecting to search articles function")
            return HttpResponseRedirect(reverse("article_search", args=[search_text]))

    # get a random 3 articles to show to the user
    articles = Article.objects.order_by("?")[:3]

    return render(request, "blog/index.html", {"articles": articles})


def articles(request):
    if request.method == "POST":
        search_text = request.POST.get("search")
        if search_text is not None and search_text != "":
            print("redirecting to search articles function")
            return HttpResponseRedirect(reverse("article_search", args=[search_text]))
    articles = Article.objects.filter(category__title="Article")
    if request.method == "POST":
        print("post")
    return render(
        request,
        "blog/articles/article_list.html",
        {"articles": articles, "category": "Article"},
    )


def article_detail(request, category, id):
    article = Article.objects.get(id=id)
    article.body = md.markdown(
        article.body,
        extensions=[
            "markdown.extensions.fenced_code",
            "markdown.extensions.extra",
            # "markdown.extensions.codehilite",
            "markdown.extensions.toc",
        ],
    )

    # for handling comments
    if request.method == "POST":
        # check for search first
        if "search" in request.POST:
            search_text = request.POST.get("search")
            if search_text is not None and search_text != "":
                print("redirecting to search articles function")
                return HttpResponseRedirect(
                    reverse("article_search", args=[search_text])
                )

        message = request.POST.get("message")
        name = request.POST.get("name")

        if message is not None and message != "":

            reply = Reply(
                article=article,
                message=message,
                date=datetime.now(),
                name=name if name is not None and name != "" else "Anonymous",
            )
            reply.save()

            # send an email
            mail.send_mail(
                "me@jakelanders.com",
                "Reply on article: {}".format(article),
                "There was a reply on article: {}\n\n{}/n- {}".format(
                    article,
                    message,
                    name if name is not None and name != "" else "Anonymous",
                ),
            )

            return HttpResponseRedirect(
                reverse("article_detail", args=[category, article.id])
            )

    # get all replies
    replies = Reply.objects.filter(article__id=id)

    # get all assets
    images = Image.objects.filter(article__id=id)
    videos = Video.objects.filter(article__id=id)

    return render(
        request,
        "blog/articles/article.html",
        {"article": article, "replies": replies, "images": images, "videos": videos},
    )


def crosscheck(request):
    if request.method == "POST":
        search_text = request.POST.get("search")
        if search_text is not None and search_text != "":
            print("redirecting to search articles function")
            return HttpResponseRedirect(reverse("article_search", args=[search_text]))
    return render(request, "blog/projects/crosscheck.html")


def article_search(request, search_text):
    if request.method == "POST":
        search_text = request.POST.get("search")
        if search_text is not None and search_text != "":
            print("redirecting to search articles function")
            return HttpResponseRedirect(reverse("article_search", args=[search_text]))
    articles = Article.objects.filter(
        Q(category__title__contains=search_text)
        | Q(tags__contains=search_text)
        | Q(title__contains=search_text)
    )

    print(articles)

    return render(
        request,
        "blog/articles/article_list.html",
        {"articles": articles, "category": "search"},
    )
