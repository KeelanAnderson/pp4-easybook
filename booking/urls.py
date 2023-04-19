from . import views
from django.urls import path
from .views import (
    CreatePostView,
    CreateServiceView,
    DeletePostView,
    DeleteServiceView,
    ManagePostView,
    PostDetail,
    PostList,
    UpdatePostView,
    UpdateServiceView,
)

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("create/", CreatePostView.as_view(), name="create_post"),
    path("<slug:slug>/update/", UpdatePostView.as_view(), name="update_post"),
    path("<slug:slug>/delete/", DeletePostView.as_view(), name="delete_post"),
    path("<slug:slug>/detail/", PostDetail.as_view(), name="post_detail"),
    path("manage_post/", ManagePostView.as_view(), name="manage_post"),
    path(
        "create_service/",
        CreateServiceView.as_view(),
        name="create_service"
        ),
    path(
        "<pk>/update_service/",
        UpdateServiceView.as_view(),
        name="update_service"
        ),
    path(
        "<pk>/delete_service/",
        DeleteServiceView.as_view(),
        name="delete_service"
        )
]
