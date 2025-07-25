from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_selection, name='home'),  # Root URL added here

    path('role/', views.role_selection, name='role_selection'),

    # Role-specific pages
    path('frontend/', views.frontend, name='frontend'),
    path('backend/', views.backend_view, name='backend'),
    path('data-scientist/', views.data_scientist_view, name='data_scientist'),
    path('cloud-engineer/', views.cloud_engineer, name='cloud_engineer'),

    # Aptitude & Quiz
    path('aptitude/', views.aptitude_view, name='aptitude'),
    path('quiz/', views.start_quiz, name='start_quiz'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),
]
