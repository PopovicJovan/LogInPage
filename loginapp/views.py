from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
import jwt
from django.contrib.auth.hashers import make_password, check_password


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self): return User.objects.all()

    def destroy(self, request, *args, **kwargs): return Response()

    def update(self, request, *args, **kwargs): return Response()

    def create(self, request, *args, **kwargs):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        username = request.data['username']
        password = make_password(request.data['password'])
        User.objects.create(username=username,
                            first_name=first_name,
                            last_name=last_name,
                            password=password)
        return Response()


class LogInSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self): return User.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.data['username'])
            if not check_password(request.data['password'], user.password):
                return Response('Credentials are wrong!')

            payload_data = {'username:': user.username,
                            'first name': user.first_name,
                            'last name': user.last_name}

            token = jwt.encode(payload_data,
                               'secret')
            return Response(token)
        except User.DoesNotExist: return Response({'Wrong info!'})
