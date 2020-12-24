from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('quiz/attempt/',views.attempt,name='attempt_quiz'),
    path('result/',views.result,name='result')
]