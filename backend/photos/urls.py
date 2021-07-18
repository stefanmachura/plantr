from django.urls import path

from photos.views import PhotoUploadView, PhotoListView

urlpatterns = [
    path("upload/", PhotoUploadView.as_view(), name="photo_upload"),
    path("list/", PhotoListView.as_view(), name="photo_list"),
]
