from .views import PostsList, PostDetailView, PostCreateView
from django.urls import path


urlpatterns = [

    path('', PostsList.as_view()),
    path('<int:pk>', PostDetailView.as_view()),
    path('create/', PostCreateView.as_view(), name='post_create'),
]