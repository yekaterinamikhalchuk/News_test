from .views import PostsList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, subscribe, unsubscribe, \
    CategoriesSubsription
from django.urls import path


urlpatterns = [

    path('', PostsList.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('subscribe/<int:pk>', subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe, name='unsubscribe'),
    path('subscription/', CategoriesSubsription.as_view(), name='subscription'),

]