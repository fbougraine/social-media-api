from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserCreateView.as_view()),
    path('posts/', PostCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),  # get post with likes/comments
    path('likes/', LikeCreateView.as_view()),
    path('shares/', ShareCreateView.as_view()),
    path('retweets/', RetweetCreateView.as_view()),
    path('comments/', CommentCreateView.as_view()),
]
