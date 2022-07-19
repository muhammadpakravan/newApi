from django.urls import path
from. views import ArticlesAPIView, ArticleAPIView, CategoryAPIArticle, CategoryAPIView, SourceAPIList, SourceAPIArticle, FilterAPIArticle, SearchArticleAPI


urlpatterns = [
    # list of all news
    path('api/Article', ArticlesAPIView.as_view(), name="Articla_Lists"),
    # pk one news
    path("api/Article/<int:pk>/", ArticleAPIView.as_view(), name="Article_detail"),
    # category lists
    path("api/category/", CategoryAPIView.as_view(), name="categor_list"),
    # category articles
    path("api/category/<str:category>/",
         CategoryAPIArticle.as_view(), name="category_Article"),
    # source list
    path("api/source/", SourceAPIList.as_view(), name="source_list"),
    # sorce articles
    path(
        "api/source/<str:source>", SourceAPIArticle.as_view(), name="source_article"),
    # filter with source and category
    path(
        "api/filter/<str:source>/<str:category>", FilterAPIArticle.as_view(), name="Filter_source_category"
    ),
    path("api/search/<str:search>",
         SearchArticleAPI.as_view(), name="Search_Article")
]
