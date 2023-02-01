from django.contrib import admin

# Register your models here.
from .models import Article, Topic, Contact, Image

# admin.site.register(Topic)
#admin.site.register(Article)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'message')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_name', 'topic_display_name','topic_identifier','topic_html_page', 'topic_slug')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'article', 'caption', 'order')

# Define the admin class
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'article_title', 'article_topic', 'article_html_page')
 
# Register the admin class with the associated model
admin.site.register(Article, ArticleAdmin)
