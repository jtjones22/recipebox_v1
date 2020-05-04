from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()

    def __str__(self):
        return self.name

    # IF we want name in url
    # def url(self):
    #     return "-".join(str(self.name).lower().split(" "))


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=30)
    instructions = models.TextField()

    def __str__(self):
        return self.title
