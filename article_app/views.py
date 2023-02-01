# Create your views here

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from django.views.decorators.common import no_append_slash
from django.core.mail import send_mail, BadHeaderError

from .models import Topic, Article, Contact, Image

def HomePageView(request):
    try:
        home_buttons = Topic.objects.all()
    except Topic.DoesNotExist:
        raise Http404('Topics does not exist')
    try:    
        home_links = Article.objects.filter(article_identifier='home-page-link')
    except Article.DoesNotExist:
        raise Http404('Articles does not exist')    
    home_page_objects = {'home_page_buttons': home_buttons, 'home_page_links': home_links}
    context_object_name = home_page_objects
    return render(request, 'article_app/home_page.html', home_page_objects)

def TrieView(request):
    topic = Topic.objects.get(topic_slug='trie-data-structure-and-algorithm-program')
    trie_articles_list = Article.objects.filter(article_topic=topic.topic_name)
    trie_articles = {'trie_articles': trie_articles_list}
    return render(request, 'article_app/trie.html', trie_articles)

def GraphView(request):
    graph_traversal = Article.objects.filter(article_identifier='graph-page-traversal-link')
    graph_path_finding = Article.objects.filter(article_identifier='graph-page-find-path-link')
    graph_articles = {'graph_traversal_programs': graph_traversal, 'graph_path_finding_finding_programs': graph_path_finding}
    return render(request, 'article_app/graph-data-structure-and-algorithm.html', graph_articles)   

def AboutUsPageView(request):
    return render(request, 'article_app/about-us.html')

def ContactUsPageView(request):
    if request.method == 'POST':
        contact = Contact()
        fName = request.POST.get('first_name')
        lName = request.POST.get('last_name')
        email = request.POST.get('email_address')
        message = request.POST.get('message')
        contact.first_name = fName
        contact.last_name = lName
        contact.email_address = email
        contact.message = message
        if(fName != '' and email != '' and message != ''): 
            contact.save()
            messages.success(request, 'Message submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')
    return render(request, "article_app/contact-us.html")

def ArticleDetailView(request, articleSlug):
    appName = 'article_app/'
    try:
        article = Article.objects.get(article_slug=articleSlug)
        images = Image.objects.filter(article=article.article_id).order_by('order')
    except Article.DoesNotExist:
        raise Http404('Graph article does not exist')
    article_object = {'article_object' : article, 'images_object' : images}
    return render(request, appName + article.article_html_page, article_object)    

def LinkedListView(request):
    ll_articles_list = Article.objects.filter(article_identifier='linked-list-programs')
    dll_articles_list = Article.objects.filter(article_identifier='doubly-linked-list-programs')
    linkedlist_articles = {'linkedlist_articles': ll_articles_list, 'doublylinkedlist_articles': dll_articles_list}
    return render(request, 'article_app/linked-list-data-structure-and-algorithm.html', linkedlist_articles)

@no_append_slash
def QueueView(request):
    topic = Topic.objects.get(topic_slug='queue-data-structure-and-algorithm-program')
    return render(request, 'article_app/queue-data-structure.html')

def BinarySearchTreeView(request):
    bst_traversal = Article.objects.filter(article_identifier='bst-page-traversal-programs')
    bst_insert_search = Article.objects.filter(article_identifier='bst-page-insert-and-search-programs')
    bst_articles = {'bst_traversal_programs': bst_traversal, 'bst_insert_search_programs': bst_insert_search}
    return render(request, 'article_app/binary-search-tree.html', bst_articles)

def ArraysView(request):
    arrays_articles_list = Article.objects.filter(article_identifier='arrays-programs')
    arrays_intro_list = Article.objects.filter(article_identifier='arrays-intro-programs')
    arrays_articles = {'arrays_programs' : arrays_articles_list, 'arrays_intro_programs': arrays_intro_list}
    return render(request, 'article_app/arrays-data-structure-and-algorithm.html', arrays_articles)

def StringView(request):
    string_search = Article.objects.filter(article_identifier='bst-page-traversal-programs')
    string_misc = Article.objects.filter(article_identifier='string-page-misc-programs')
    string_articles = {'string_search_programs': string_search, 'string_misc_programs': string_misc}
    return render(request, 'article_app/string-data-structure-and-algorithm.html',string_articles)

def BinaryTreeView(request):
    bt_articles_list = Article.objects.filter(article_identifier='binary-tree-programs')
    bt_articles = {'bt_articles': bt_articles_list}
    return render(request, 'article_app/binary-tree-data-structure-and-algorithm.html', bt_articles)

def StackView(request):
    topic = Topic.objects.get(topic_slug='stack-data-structure-and-algorithm-program')
    return render(request, 'article_app/stack-data-structure-and-algorithm.html')

def DynamicProgrammingView(request):
    dp_articles_list = Article.objects.filter(article_identifier='dynamic-programming-programs')
    dp_articles = {'dp_articles': dp_articles_list}
    return render(request, 'article_app/dynamic-programming.html', dp_articles)

def RecursionView(request):
    topic = Topic.objects.get(topic_slug='recursion-concept-or-program-algorithm')
    images = Image.objects.filter(image='recursion.jpeg').order_by('order')
    article_object = {'images_object' : images}
    return render(request, 'article_app/recursion-concepts-and-program.html', article_object)

def HomePageLinksView(request):
    home_links_list = Article.objects.filter(article_identifier='home-page-link')
    home_page_links = {'home_page_links': home_links_list}
    return render(request, 'article_app/linked-list.html', home_page_links)

def BSTView(request):
    article = Article.objects.get(article_slug='binary-search-tree-or-bst-inorder-traversal-recursive-program')
    return render(request, article.article_html_page, article)