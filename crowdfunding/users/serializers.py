from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser, Profile, Puns


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    def create(self, validated_data):
          return CustomUser.objects.create(**validated_data)      

# CREATE A USER ACCOUNT
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


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