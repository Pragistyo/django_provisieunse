from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:doctor_id>/show/', views.show, name='detail_doctor'),
]