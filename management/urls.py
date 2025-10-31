from django.urls import path
from . import views

# app_name = 'management'

urlpatterns = [
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<str:student_id>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<str:student_id>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('fees/', views.FeeStructureListView.as_view(), name='fee_structure_list'),

    path('fees/<int:pk>/update/', views.FeeStructureUpdateView.as_view(), name='fee_update'),
    path('payments/', views.PaymentRecordView.as_view(), name='payment_record'),
]

