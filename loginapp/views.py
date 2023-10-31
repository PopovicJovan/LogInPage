from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
import jwt



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
            user = User.objects.get(first_name=request.data['first_name'],
                                    password=request.data['password'])

            payload_data = {'username:': user.first_name,
                            'password:': user.password  }
            token = jwt.encode(payload_data,
                               'secret')
            return Response(token)
        except User.DoesNotExist: return Response({'Wrong info!'})


