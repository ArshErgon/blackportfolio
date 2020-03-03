from django.db import models

class AboutModel(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about[:50]

class LearntModel(models.Model):
    learntmsg = models.TextField()

    def __str__(self):
        return self.learntmsg[:50]

class SkillModel(models.Model):
    python = models.CharField(max_length=3)
    django = models.CharField(max_length=3)
    html = models.CharField(max_length=3)
    css = models.CharField(max_length=3)
    scss = models.CharField(max_length=3)
    javascript = models.CharField(max_length=3)
    photoshop = models.CharField(max_length=3)
    illustrator = models.CharField(max_length=3)
    mobilescreen = models.CharField(max_length=100000)
    webscreen = models.CharField(max_length=1000000)

    def __str__(self):
        return self.python


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phnumber = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SeoModel(models.Model):
    head_tag = models.TextField()

    def __str__(self):
        return self.head_tag[:50]