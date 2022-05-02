from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import ProductForm
from .models import Post, Category


class PostsList(ListView, FormMixin):
    model = Post
    template_name = 'news/news_list.html'
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

        return context


# дженерик для получения деталей о товаре
class PostDetailView(DetailView):
    template_name = 'news/post_detail.html'
    queryset = Post.objects.all()


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'news/post_create.html'
    form_class = ProductForm
    permission_required = ('news.add_post',)


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'news/post_create.html'
    form_class = ProductForm
    permission_required = ('news.change_post',)

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('pk')
        return Post.objects.get(pk=post_id)


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    permission_required = ('news.delete_post',)


@login_required
def subscribe(request, **kwargs):
    post = Post.objects.get(pk=kwargs['pk'])
    user = request.user
    category_id = kwargs['pk']
    for category in post.categories.all():
        if user not in category.subscribers.all():
            category.subscribers.add(user)
    return redirect('/news')


@login_required
def unsubscribe(request, **kwargs):
    post = Post.objects.get(pk=kwargs['pk'])
    user = request.user
    category_id = kwargs['pk']
    for category in post.categories.all():
        if user in category.subscribers.all():
            category.subscribers.delete(user)
    return redirect('/news')





