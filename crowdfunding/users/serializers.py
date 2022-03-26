from rest_framework import serializers
from .models import CustomUser, Profile, Puns


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    def create(self, validated_data):
          return CustomUser.objects.create(**validated_data)      

class ProfileSerializer(serializers.Serializer):
    profile_img = serializers.URLField()
    name = serializers.CharField(max_length=200)
    bio = serializers.CharField(max_length=600)
    link = serializers.URLField()

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

class PunsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    post = serializers.CharField(max_length=200)
    date_posted = serializers.DateTimeField()

    def create(self, validated_data):
        return Puns.objects.create(**validated_data)