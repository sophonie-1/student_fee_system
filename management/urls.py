from django.urls import path
from . import views

# app_name = 'management'

urlpatterns = [
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<str:student_id>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
]