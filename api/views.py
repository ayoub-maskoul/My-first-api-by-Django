from django.shortcuts import render
from rest_framework import viewsets
from api.models import Student
from api.serializers import StudenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def list_student(request):
    # GET
    if request.method == 'GET':
        guests = Student.objects.all()
        serializer = StudenSerializer(guests, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = StudenSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

# GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def student(request, id):
    try:
        guest = Student.objects.get(id=id)
    except Student.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = StudenSerializer(guest)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = StudenSerializer(guest, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        guest.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



#  view set GET POST DELETE PUT
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudenSerializer