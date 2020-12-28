from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from profiles_api import permissions
from profiles_api import models
from profiles_api import serializers

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        Friends=[
                "elango",
                "vishal",
                "lokesh"
                ]
        return Response({"welcome":"hello!","Friends":Friends})
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Welcome {name}'
            return Response({"message":message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        return Response({"method":"put"})

    def patch(self,request,pk=None):
        return Response({"method":"patch"})

    def delete(self,request,pk=None):
        return Response({'method':'delete'})

class HelloViewset(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        places = [
                "USA",
                "INDIA",
                "CHINA",
                "RUSSIA"
                ]
        return Response({"message":"Hello","places":places})

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello! {name}'
            return Response({"message":message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        return Response({"HTTP_METHOD":"GET"})

    def update(self,request,pk=None):
        return Response({"HTTP_METHOD":"PUT"})

    def partial_update(self,request,pk=None):
        return Response({"HTTP_METHOD":"PATCH"})

    def destroy(self,request,pk=None):
        return Response({"HTTP_METHOD":"DELETE"})


class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerilizer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name","email")

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserFeedApiViewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = (serializers.UserFeedItemSerializer)
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnFeed,IsAuthenticated,)
    # IsAuthenticatedOrReadOnly

    def perform_create(self,serializer):
        serializer.save(userprofile = self.request.user)
