from django.contrib import admin
from .models import Student, FeeStructure, Payment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'name', 'program', 'campus', 'year_of_study', 'get_balance', 'get_status']
    list_filter = ['program', 'campus', 'year_of_study']

@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ['program', 'year', 'total_fee']
    list_filter = ['program', 'year']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'student', 'amount', 'date']
    list_filter = ['date', 'student__program']