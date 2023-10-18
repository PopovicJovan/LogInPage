from rest_framework import serializers
from .models import User as Myuser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Myuser
        fields = '__all__'
