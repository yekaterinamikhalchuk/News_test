from .views import PostsList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, subscribe, unsubscribe, \
    CategoriesSubsription, Index
from django.urls import path, include
from django.views.decorators.cache import cache_page
# from rest_framework import routers
# import views

# router = routers.DefaultRouter()
# router.register(r'posts', views.PostViewset)
# router.register(r'authors', views.AuthorViewset)
# router.register(r'categories', views.CategoryViewest)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # подключаем встроенные эндопинты для работы с локализацией
    path('', cache_page(60)(PostsList.as_view())),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('subscribe/<int:pk>', subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe, name='unsubscribe'),
    path('subscription/', CategoriesSubsription.as_view(), name='subscription'),
    path('language/', Index.as_view()),

]