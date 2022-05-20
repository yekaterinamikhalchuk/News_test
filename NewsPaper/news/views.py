
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse

from django.shortcuts import redirect, render

from django.core.cache import cache
from django.views import View

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import PostForm, CategoryForm
from .models import Post, Category, Author
from django.utils import timezone
import pytz  # импортируем стандартный модуль для работы с часовыми поясами


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

    def get_object(self, *args, **kwargs):  # переопределяем метод получения объекта, как ни странно
        obj = cache.get(f'post-{self.kwargs["pk"]}',
                        None)  # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.

        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)

        return obj


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



class Index(View):
    def get(self, request):
        curent_time = timezone.now()

        # .  Translators: This message appears on the home page only
        models = Post.objects.all()

        context = {
            'models': models,
            'current_time': curent_time,
            'timezones': pytz.common_timezones,  # добавляем в контекст все доступные часовые пояса
            'LANGUAGE_CODE': request.LANGUAGE_CODE
        }

        return HttpResponse(render(request, 'default.html', context))

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')





