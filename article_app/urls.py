from django.urls import path
from .views import  AboutUsPageView, HomePageView, ArticleDetailView, TrieView, GraphView, LinkedListView, QueueView, BinarySearchTreeView \
     ,ArraysView, StringView, BinaryTreeView, ContactUsPageView, StackView, DynamicProgrammingView, RecursionView, BSTView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about-us', AboutUsPageView, name="AboutUsPageView"),
    path('contact-us', ContactUsPageView, name="ContactUsPageView"),
    path('', HomePageView, name="HomePageView"),
    path('graph-data-structure-and-algorithm', GraphView, name='GraphView'),
    path('trie-data-structure-and-algorithm-program', TrieView, name='TrieView'),
    path('linked-list-data-structure-and-algorithm', LinkedListView, name='LinkedListView'),
    path('queue-data-structure-and-algorithm-program', QueueView, name='QueueView'),
    path('binary-search-tree-or-bst-data-structure-and-algorithm-program', BinarySearchTreeView, name='BinarySearchTreeView'),
    path('arrays-data-structure-and-algorithm', ArraysView, name='ArraysView'),
    path('string-data-structure-and-algorithm-program', StringView, name='StringView'),
    path('binary-tree-or-bt-data-structure-and-algorithm-program', BinaryTreeView, name='BinaryTreeView'),
    path('stack-data-structure-and-algorithm-program', StackView, name='StackView'),
    path('dynamic-programming-concepts-or-algorithm', DynamicProgrammingView, name='DynamicProgrammingView'),
    path('recursion-concept-or-program-algorithm', RecursionView, name='RecursionView'),
    
    path('binary-search-tree-or-bst-inorder-traversal-recursive-program', BSTView, name='BSTView'),
    path('<slug:articleSlug>',ArticleDetailView, name='ArticleDetailView'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)