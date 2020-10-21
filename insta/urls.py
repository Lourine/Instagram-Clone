from django.urls import path
from . import views
from .views import (
Home, ViewPost, CreatePost,
UpdatePost,DeletePost, ViewProfile,
CreateComment,DeleteComment,
LikePostAPI, ViewLikes, ViewNotifications
)


urlpatterns = [
    path('', Home.as_view(), name='insta-home'),
    path('search/', views.search, name='search'),
    path('post/<int:pk>/', ViewPost.as_view(), name='insta-detail'),
    path('post/new/', CreatePost.as_view(), name='insta-create'),
    path('post/<int:pk>/update', UpdatePost.as_view(), name='insta-update'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name='insta-delete'),
    path('user/<str:username>/', ViewProfile.as_view(), name='insta-profile'),
    path('post/<int:pk>/comment/', CreateComment.as_view(), name='insta-comment'),
    path('comment/<int:pk>/delete/', DeleteComment.as_view(), name='insta-delete_comment'),
    path('post/<int:pk>/like_api/', LikePostAPI.as_view(), name='insta-post_like_api'),
    path('post/<int:pk>/likes/', ViewLikes.as_view(), name='insta-post_likes'),
    path('notifications/', ViewNotifications.as_view(), name='insta-notifications'),
]
