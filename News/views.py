from unicodedata import category
from rest_framework import generics
from .serializers import ArticleSerializer, CategorySerializer, SourceSerializer
from . models import Source, Article, Category
from simple_search import search_filter
# Create your views here.


class ArticlesAPIView(generics.ListAPIView):

    serializer_class = ArticleSerializer

    def get_queryset(self):

        return Article.objects.filter(status="p").order_by('-data_added')


class ArticleAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.filter(status="p").order_by('-data_added')
    serializer_class = ArticleSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIArticle(generics.ListAPIView):

    serializer_class = ArticleSerializer

    def get_queryset(self):

        category = self.kwargs['category']
        return Article.objects.filter(category__name=category).filter(status="p").order_by('-data_added')


class SourceAPIList(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceAPIArticle(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):

        source = self.kwargs["source"]
        return Article.objects.filter(source__name=source).filter(status="p").order_by('-data_added')


class FilterAPIArticle(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):

        source = self.kwargs["source"]
        category = self.kwargs["category"]

        return Article.objects.filter(source__name=source).filter(category__name=category).filter(status="p").order_by('-data_added')


class SearchArticleAPI(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        search_fields = ['^title', 'text']
        query = self.kwargs['search']
        return Article.objects.filter(search_filter(search_fields, query)).filter(status='p').order_by('-data_added')
