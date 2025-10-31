from django.urls import path
from . import views

# app_name = 'management'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student_list'),
    path('students/<str:student_id>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<str:student_id>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('fees/', views.FeeStructureListView.as_view(), name='fee_structure_list'),

    path('fees/<int:pk>/update/', views.FeeStructureUpdateView.as_view(), name='fee_update'),
    path('payments/', views.PaymentRecordView.as_view(), name='payment_record'),

    path('reports/student/', views.PerStudentReportView.as_view(), name='per_student_report'),
    path('reports/program/', views.PerProgramReportView.as_view(), name='per_program_report'),
    path('reports/overall/', views.OverallSummaryView.as_view(), name='overall_summary'),
    path('export/', views.ExportCSVView.as_view(), name='export_csv'),
]

