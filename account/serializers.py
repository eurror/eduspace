from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'token': serializers.SerializerMethodField(),
            'refresh': serializers.SerializerMethodField(),
        }

    def get_token(self, validated_data: dict):
        user = validated_data.get('user')
        token: RefreshToken = RefreshToken.for_user(user)
        return str(token.access_token)

    def get_refresh(self, validated_data: dict):
        token = validated_data.get('token')
        return str(token)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
