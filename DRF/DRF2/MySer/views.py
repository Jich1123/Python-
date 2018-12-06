from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from MySer.models import *
from MySer.serializers import *
from rest_framework.response import Response
# Create your views here.

class StudentGenAPIView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request):
        # ser = self.get_serializer(self.get_queryset(), many=True)
        ser = self.get_serializer(self.queryset.all(), many=True)
        return Response(data=ser.data)

class StudentVS(viewsets.ModelViewSet):
    pass

class StudentAPIView(APIView):
    def get(self, request):
        # print("This is in APIView get")
        # return None
        stus = Student.objects.all()
        ser = StudentSerializer(stus, many=True)
        return Response(data=ser.data)

from rest_framework.viewsets import ModelViewSet

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        print("重写")
        rst = super(StudentViewSet, self).list(request,*args, **kwargs)
        return rst

