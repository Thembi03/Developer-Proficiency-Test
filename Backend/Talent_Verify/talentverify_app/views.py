from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# talentverify_app/views.py

from rest_framework import viewsets
from .models import Company, Department, Employee
from .serializers import CompanySerializer, DepartmentSerializer, EmployeeSerializer
from .pagination import StandardResultsSetPagination

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'registration_date', 'contact_person']
    ordering_fields = ['name', 'registration_date']

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'company']
    ordering_fields = ['name', 'company']

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'department', 'role']
    ordering_fields = ['name', 'department', 'role', 'date_started']

# Create your views here.
