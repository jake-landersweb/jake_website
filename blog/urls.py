from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("", views.index, name="index"),
    path("flutter/", views.flutter, name="flutter"),
    path("swiftui/", views.swiftui, name="swiftui"),
    path("machine-learning/", views.machine_learning, name="machine-learning"),
    path("<str:category>/<int:id>/", views.article_detail, name="article_detail",),
    path("projects/crosscheck", views.crosscheck, name="crosscheck"),
    path("search/<slug:search_text>/", views.article_search, name="article_search",),
]

