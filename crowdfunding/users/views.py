from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from .models import CustomUser, Profile, Puns
from .serializers import CustomUserSerializer, PunsSerializer, RegisterSerializer, ProfileSerializer, ProfileDetailSerializer
from projects.permissions import IsOwnerOrReadOnly

class CustomUserList(APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CustomUserDetail(APIView):

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

# create new account: the view that links with serializer
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny,]
    queryset = CustomUser.objects.all()

class ProfileDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
        ]
    
    def get(self, request, pk):
        profile = Profile.objects.all()
        serializer = ProfileDetailSerializer(profile, many=True)
        return Response(serializer.data)

# to edit profile

    def put(self, request, pk):
        serializer = ProfileDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)



class PunsList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
        ]

    def get(self, request):
        puns = Puns.objects.all()
        serializer = PunsSerializer(puns, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PunsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)