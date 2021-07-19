from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from users.serializers import UserSerializer


class UserHomepage(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            "user": str(request.user),  # `django.contrib.auth.User` instance.
            "auth": str(request.auth),  # None
        }
        return Response(content)


class RegisterUserView(CreateAPIView):
    serializer_class = UserSerializer
