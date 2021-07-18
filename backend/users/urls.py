from django.urls import path

from users.views import UserHomepage

urlpatterns = [
    path("home", UserHomepage.as_view(), name="homepage"),
]
