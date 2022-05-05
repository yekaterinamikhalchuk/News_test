
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import redirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import PostForm, CategoryForm
from .models import Post, Category, Author


class PostsList(ListView, FormMixin):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('creation_date')
    paginate_by = 10
    form_class = PostForm

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
    form_class = PostForm

    model = Post
    # fields = ['news_type', 'post_title', 'post_text', 'categories']
    permission_required = ('news.add_post',)

    # def form_valid(self, form):
    #     user_id = self.request.user.id
    #     author = Author.objects.get(user_id=user_id)
    #     form.instance.author = author
    #     return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = Author.objects.get(user_id=self.request.user.id)
        return initial


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'news/post_create.html'
    form_class = PostForm
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
    category = Category.objects.get(pk=kwargs['pk'])
    user = request.user
    if user not in category.subscribers.all():
        category.subscribers.add(user)

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def unsubscribe(request, **kwargs):
    category = Category.objects.get(pk=kwargs['pk'])
    user = request.user
    if user in category.subscribers.all():
        category.subscribers.remove(user)
    return redirect(request.META.get('HTTP_REFERER', '/'))


class CategoriesSubsription(LoginRequiredMixin, ListView, FormMixin):
    model = Category
    template_name = 'news/subscription.html'
    context_object_name = 'subscription'
    form_class = CategoryForm

    def get_context_data(self,
                         **kwargs):
        context = super().get_context_data(**kwargs)
        return context



