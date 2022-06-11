from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from .models import CustomUser, Puns
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, PunsSerializer, RegisterSerializer, PunsDetailSerializer
# from projects.permissions import IsOwnerOrReadOnly

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
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
#         # IsOwnerOrReadOnly
        ]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserDetailSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)    
        data = request.data 
        serializer = CustomUserDetailSerializer(
            instance = user, 
            data = data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# create new account: the view that links with serializer
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny,]
    queryset = CustomUser.objects.all()

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
    
    def delete(self, request, pk):
        puns = self.get_object(pk)
        puns.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PunsDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        ]
    
    def get_object(self, pk):
        try:
            return Puns.objects.get(pk=pk)
        except Puns.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        puns = self.get_object(pk)
        serializer = PunsDetailSerializer(puns)
        return Response(serializer.data)

    def delete(self, request, pk):
        puns = self.get_object(pk)
        puns.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)