
from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register('student', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('liststudent/',views.list_student ),
    path('liststudent/<int:id>',views.student)
]
