from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, PageSerializer, LoanSerializer
from .models import User, Page, Loan

# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PageView(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()

class LoanView(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()