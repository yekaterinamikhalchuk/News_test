from .views import PostsList, PostDetail
from django.urls import path


urlpatterns = [

    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]