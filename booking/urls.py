from . import views
from django.urls import path
from .views import PostList, PostDetail, CreatePostView, UpdatePostView, DeletePostView, ManagePostView, CreateServiceView, UpdateServiceView, DeleteServiceView


urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("create/", CreatePostView.as_view(), name="create_post"),
    path("<slug:slug>/update/", UpdatePostView.as_view(), name="update_post"),
    path("<slug:slug>/delete/", DeletePostView.as_view(), name="delete_post"),
    path("<slug:slug>/detail/", PostDetail.as_view(), name="post_detail"),
    path("manage_post/", ManagePostView.as_view(), name="manage_post"),
    path("create_service/", CreateServiceView.as_view(), name="create_service"),
    path("<int:post>/update/", UpdateServiceView.as_view(), name="update_service"),
    path("<int:post>/delete/", DeleteServiceView.as_view(), name="delete_service"),
]