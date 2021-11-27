from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField("date posted")
    description = models.TextField(default="")
    body = models.TextField()
    tags = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to="assets/", default="", blank=True)
    video = models.FileField(upload_to="assets/", default="", blank=True)

    def get_tags(self):
        if self.tags == "":
            return ""
        else:
            list_tags = self.tags.split(",")
            tag_str = ""
            for i in list_tags:
                if i == list_tags[-1]:
                    tag_str = tag_str + "#{}".format(i)
                else:
                    tag_str = tag_str + "#{}, ".format(i)

            return tag_str

    def get_tags_small(self):
        if self.tags == "":
            return ""
        else:
            list_tags = self.tags.split(",")
            list_tags = list_tags[:3]
            tag_str = ""
            for i in list_tags:
                if i == list_tags[-1]:
                    tag_str = tag_str + "#{}".format(i)
                else:
                    tag_str = tag_str + "#{}, ".format(i)

            return tag_str

    def __str__(self):
        return self.title


class Reply(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField("date posted")
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return "Reply on article: {}".format(self.article)

