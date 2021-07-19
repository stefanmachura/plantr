from django.urls import path

from users.views import UserHomepage, RegisterUserView

urlpatterns = [
    path("home", UserHomepage.as_view(), name="homepage"),
    path("register", RegisterUserView.as_view(), name="register"),
]
