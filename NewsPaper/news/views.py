from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView

from .filters import PostFilter
from .forms import ProductForm
from .models import Post


class PostsList(ListView, FormMixin):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('creation_date')
    paginate_by = 10
    form_class = ProductForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return PostFilter(self.request.GET, queryset=queryset).qs

    def get_context_data(self,
                         **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,
                                       queryset=self.get_queryset())
        context['form'] = ProductForm()
        return context


# дженерик для получения деталей о товаре
class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = ProductForm




