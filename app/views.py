from django.shortcuts import render

# Create your views here.


from app.models import *

from app.serializers import *


from rest_framework.views import APIView

from rest_framework.response import Response

# from rest_framework.generics.views import ViewSets


class StudentDetails(APIView):
    def get(self,request,id):
        so = student.objects.get(id=id)
        s = StudentSerializer(so)
        return Response(s.data)
    def put(self,request,id):
        so   =  student.objects.get(id=id)
        serializer = StudentSerializer(so,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data is updated succesfully")
        else:
            return Response(serializer.errors)
    def patch(self,request,id):
        so   =  student.objects.get(id=id)
        serializer = StudentSerializer(so,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("data is updated succesfully")
        else:
            return Response(serializer.errors)
    def delete(self,request,id):
        so   =  student.objects.get(id=id)
        so.delete()
        return Response("data deleted successfully")






















# class CN(ViewSets.ModelViewSets):
#     queryset = students.objects.all()
#     serializer_class = StudentSerializer 

        

