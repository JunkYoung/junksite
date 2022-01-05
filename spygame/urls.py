from django.urls import path
from . import views

urlpatterns = [
    path('question', views.question_list, name='question_list'),
    path('', views.index, name='index'),
]