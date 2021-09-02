from django.db import models

class AboutModel(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about[:50]

class LearntModel(models.Model):
    learntmsg = models.TextField()

    def __str__(self):
        return self.learntmsg[:50]

class Project(models.Model):
    project_image = models.CharField(max_length=250)
    project_name = models.CharField(max_length=100)
    project_body = models.TextField()

    def __str__(self):
        return self.project_name

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

class SocialMedia(models.Model):
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    quora = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100, default=True)

    def __str__(self):
        return self.instagram
        
class SeoModel(models.Model):
    head_tag = models.TextField()

    def __str__(self):
        return self.head_tag[:50]