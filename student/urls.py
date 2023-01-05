from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-student', views.student_submit, name='add-student'),
    path('delete-student/<str:pk>/', views.delete_student, name='delete-student'),
]