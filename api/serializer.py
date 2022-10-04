from msilib.schema import Class
from pyexpat import model
from rest_framework import serializers
from wallet.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
     model = User
     fields = ('first_name', 'last_name', 'email', 'password','age', 'address')