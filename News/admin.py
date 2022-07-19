import django
from django.contrib import admin
from .models import Category, category, Source, Article

# Register your models here.

admin.site.site_header = ' '


@admin.action(description='همه ی اخبار را در حالت انتشار قرار بده')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


@admin.action(description='همه ی اخبار را در حالت بایگانی قرار بده')
def make_withdrow(modeladmin, request, queryset):
    queryset.update(status='d')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published, make_withdrow]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


class SourceAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


admin.site.register(Article, ArticleAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Source, SourceAdmin)
