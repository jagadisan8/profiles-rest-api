from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self,request,format=None):
        Friends=[
                "elango",
                "vishal",
                "lokesh"
                ]
        return Response({"welcome":"hello!","Friends":Friends})
