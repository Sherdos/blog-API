from dataclasses import field
from rest_framework import serializers
from apps.users.models import User 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'profile_image', 'phone')

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 255, write_only=True)
    email = serializers.CharField(max_length = 255, write_only=True)
    password = serializers.CharField(max_length = 255, write_only=True)
    password2 = serializers.CharField(max_length = 255, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли отличаются"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',  'profile_image', 'phone')