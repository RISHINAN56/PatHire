from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_selection, name='role_selection'),
    path('frontend/', views.frontend, name='frontend'),
    path('backend/', views.backend_view, name='backend'),
    path('aptitude/', views.aptitude_view, name='aptitude'),
    path('quiz/', views.start_quiz, name='start_quiz'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),
    path('aptitude-quiz/', views.start_quiz),


]
