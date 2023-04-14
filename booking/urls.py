from . import views
from django.urls import path
from .views import PostList, PostDetail, BookingList, CreatePostView, UpdatePostView, DeletePostView, manage_post


urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("create/", CreatePostView.as_view(), name="create_post"),
    path("<slug:slug>/update/", UpdatePostView.as_view(), name="update_post"),
    path("<slug:slug>/delete/", DeletePostView.as_view(), name="delete_post"),
    path("<slug:slug>/detail/", PostDetail.as_view(), name="post_detail"),
    path("manage_post/", manage_post, name="manage_post"),
    path("book/<int:service_id>/", BookingList.as_view(), name="book"),
]