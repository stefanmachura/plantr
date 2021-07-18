from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView

from django.http import HttpResponse

from posts.models import Post

from photos.serializers import PhotoSerializer
from photos.models import Photo

from photos.tasks import upload_photo_to_s3


class PhotoUploadView(CreateAPIView):
    """ not needed for now, to be refactored"""
    def create(self, request):
        p = Post.objects.get(pk=1)
        request.data["post"] = p.pk
        serializer = PhotoSerializer(data=request.data)
        serializer.is_valid(True)
        serializer.save()
        upload_photo_to_s3.delay()
        return HttpResponse(status=status.HTTP_201_CREATED)


class PhotoListView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
