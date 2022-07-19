import imp
from rest_framework import serializers

from News.models import Article, Source, Category


class ArticleSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    source_name = serializers.CharField(source='source.name')

    class Meta:
        model = Article
        fields = ("id", "title", "text", "image", "data_added",
                  "status", "writer", "category_name", "source_name")


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ("name", "url")


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("id", "name")
