from django.urls import path

from photos.views import PhotoListView, celery

urlpatterns = [
    path("", PhotoListView.as_view(),name="photos_list"),
    path("lol/", celery)
]