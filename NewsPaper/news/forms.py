from django import forms
from django.forms import ModelForm, BooleanField
from .models import Post, Category
from django import forms

class PostForm(ModelForm):
    check_box = BooleanField(label='Confirm changes')

    class Meta:
        model = Post
        fields = ['news_type', 'post_title', 'post_text',  'categories','author']
        widgets = {'author' : forms.HiddenInput()}


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['category_name']