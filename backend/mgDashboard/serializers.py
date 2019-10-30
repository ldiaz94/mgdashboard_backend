from rest_framework import serializers
from .models import User, Page, Loan

# Register your models here.
class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class PageSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Page
        fields = ('title', 'type', 'url')

class LoanSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Loan
        fields = ('name', 'loan', 'deposit', 'ltv', 'term', 'outstanding')