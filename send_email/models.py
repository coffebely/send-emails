from django.db import models


class File(models.Model):

    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Person(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()


class Log(models.Model):

    log = models.JSONField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)

