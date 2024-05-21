from django.http import JsonResponse
from product.models import ProductModel
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializer import ProductSerializer
from rest_framework.views import APIView
from rest_framework import generics,permissions , authentication


# class api_views(APIView):

#     def get(self,request,*agrs,**kwrags):
#         permission_classes = [permissions]
#         data = ProductModel.objects.all()
#         serializer = ProductSerializer(data,many=True)
#         return Response(serializer.data)
    
#     def post (self,request,*agrs,**kwrags):

#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=201)
#         return Response(serializer.errors,status=400)
    


class create_view(generics.CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class List_views (generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class api_views(generics.RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

