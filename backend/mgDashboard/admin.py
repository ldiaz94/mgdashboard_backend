from django.contrib import admin
from .models import User, Page, Loan

# Register your models here.
class UserAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'last_name')

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'url')

class LoanAdmin(admin.ModelAdmin):
    list_display = ('name', 'loan', 'deposit','ltv','term','outstanding')

admin.site.register(User, UserAdmin) 
admin.site.register(Page, PageAdmin) 
admin.site.register(Loan, LoanAdmin)