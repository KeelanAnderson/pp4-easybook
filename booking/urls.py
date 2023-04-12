from . import views
from django.urls import path
from .views import PostList, PostDetail, BookingList, CreatePostView

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("create/", CreatePostView.as_view(), name="create_post"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("book/<int:service_id>/", BookingList.as_view(), name="book"),
]