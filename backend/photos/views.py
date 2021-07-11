from rest_framework.generics import ListCreateAPIView, GenericAPIView

from django.http import HttpResponse

from photos.serializers import PhotoSerializer
from photos.models import Photo

from photos.tasks import debug_task

class PhotoListView(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

def celery(request):
    debug_task.delay()
    return HttpResponse("FINISHED")