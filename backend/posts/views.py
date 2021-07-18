from rest_framework import serializers, status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from posts.serializers import PostSerializer, PostCreateSerializer, PostViewSerializer
from posts.models import Post


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostViewSerializer


class CurrentUserPostListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostViewSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(creator=user)


class CreatePostView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostCreateSerializer

    def create(self, request):
        request.data["creator"] = request.user.pk
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
