from django.forms import SelectDateWidget
from django_filters import FilterSet, DateFilter, ChoiceFilter, CharFilter
from .models import Post


class PostFilter(FilterSet):
    creation_date = DateFilter(field_name='creation_date',
                               lookup_expr='gt',
                               label='Published after',
                               widget=SelectDateWidget)
    post_title = CharFilter(label='Title', lookup_expr='icontains')
    post_text = CharFilter(label='Text', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = (
            'post_title',
            'post_text',
            'creation_date',
            'author')
