from django.contrib import admin

from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['author', 'post_title', 'creation_date', 'post_rating']
    list_filter = ('categories__category_name', 'news_type', 'author', 'creation_date')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('author', 'category__name')


class AuthorAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['user', 'user_rating']
    list_filter = ('user', )  # добавляем примитивные фильтры в нашу админку
    search_fields = ('user', )

class CommentAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['comment_user', 'comment_post', 'creation_date_comment', 'comment_text', 'comment_rating']
    list_filter = ('comment_user', 'creation_date_comment')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('comment_user',)


class PostCategoryAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['post', 'category']





admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Author, AuthorAdmin)
# Register your models here.
