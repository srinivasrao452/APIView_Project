
from django.shortcuts import render

from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

class EmployeeListView(APIView):
    def get(self,request):
        emps = Employee.objects.all()

        serializer = EmployeeSerializer(emps,many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class EmployeeDetailView(APIView):
    def get(self,request,id):
        try:
            emp = Employee.objects.get(eno=id)
        except Employee.DoesNotExist:
            return Response('Record Not found')
        else:
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data,
                            status=status.HTTP_200_OK)


    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(eno=id)
        except Employee.DoesNotExist:
            emp = None
        return emp


    def put(self,request,id):
        emp = self.get_object_by_id(id)
        if emp is None:
            return Response('Record is not available to update')
        else:
            serializer = EmployeeSerializer(emp , data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        emp = self.get_object_by_id(id)

        if emp is None:
            return Response('Record is not available to Deleting',
                            status=status.HTTP_404_NOT_FOUND)
        else:
            emp.delete()
            return Response('Record deleted successfully',
                            status=status.HTTP_204_NO_CONTENT)































