from posts.models import Post
from photos.models import Photo
from photos.tasks import upload_photo_to_s3

from users.serializers import UserSerializer
from photos.serializers import PhotoSerializer

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description", "creator"]


class PostCreateSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "title", "description", "creator", "photos"]

    def create(self, validated_data):
        photos = validated_data.pop("photos")
        instance = Post.objects.create(**validated_data)
        for photo in photos:
            photo["post"] = instance
            new_photo = Photo.objects.create(**photo)
            upload_photo_to_s3.delay(new_photo.pk)
        return instance


class PostViewSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "title", "description", "creator", "photos"]
