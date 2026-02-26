from rest_framework import serializers
from .models import Department, Employee


class DepartmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'name', 'parent']


class EmployeeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'position', 'department', 'hired_at']