from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def destroy(self, request, *args, **kwargs):
        return Response()

    def update(self, request, *args, **kwargs):
        return Response()


class LogInSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            User.objects.get(first_name=request.data['first_name'],
                             password=request.data['password'])
            return Response('You are logged in', status=200)
        except User.DoesNotExist:
            return Response()
