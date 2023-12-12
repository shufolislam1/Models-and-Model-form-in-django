from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<int:age>', views.delete_student, name="delete_student")
]
