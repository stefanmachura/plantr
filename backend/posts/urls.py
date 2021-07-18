from django.urls import path

from posts.views import CreatePostView, PostListView, CurrentUserPostListView

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("my", CurrentUserPostListView.as_view(), name="my_posts"),
    path("new", CreatePostView.as_view(), name="create_post"),
]
