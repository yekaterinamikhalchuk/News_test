from django.forms import ModelForm, BooleanField
from .models import Post, Category


class ProductForm(ModelForm):
    check_box = BooleanField(label='Confirm changes')

    class Meta:
        model = Post
        fields = ['news_type', 'post_title', 'post_text', 'author', 'categories']


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['category_name']