from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('student-form/',views.studentForm,name='studentform'),
    path('student-list/',views.studentList,name='studentlist'),
    path('student-delete/<int:id>',views.studentDelete,name='studentDelete'),
    path('student-update/<int:id>',views.studentUpdate,name='studentUpdate'),
]
