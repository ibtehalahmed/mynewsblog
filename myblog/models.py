from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_name = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.tag_name

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_img = models.ImageField(upload_to='uploads/')
    post_content = models.TextField()
    post_publish_date = models.DateTimeField(auto_now_add=True)
    post_category = models.CharField(max_length=15)
    post_link = models.SlugField(max_length=200,default='NULL')
    post_tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.post_title