import uuid
from django.db import models
from django.utils import timezone
from django.db import models
from django.db.models import FileField, ImageField

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(primary_key=True, max_length=1000)
    topic_display_name = models.CharField(max_length=1000)
    topic_identifier = models.CharField(max_length=1000, null=True)
    topic_html_page = models.CharField(max_length=1000, null=True)
    topic_slug = models.SlugField(null=True, unique=True, max_length=1000) 

class Article(models.Model):
    article_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article_name = models.CharField(max_length=1000, null=True) # this is similar to title, but just for convenience we have this field
    article_title = models.CharField(max_length=1000, null=True)
    article_topic = models.ForeignKey(Topic, default='no_topic', on_delete=models.SET_DEFAULT)
    article_content = models.TextField() # for huge content textfield is unrestricted text
    article_author = models.CharField(max_length=1000, null=True)
    article_identifier = models.CharField(max_length=1000, null=True)
    article_html_page = models.CharField(max_length=1000, null=True)
    article_html_page_path = models.CharField(max_length=1000, null=True)
    article_slug = models.SlugField(null=True, unique=True, max_length=1000)  # new
    date_posted = models.DateTimeField(default=timezone.now) #

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(max_length=1000, upload_to='')
    caption = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name