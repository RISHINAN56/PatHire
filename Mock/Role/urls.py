from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_selection, name='home'),
    path('role/', views.role_selection, name='role_selection'),
    path('quiz/', views.start_quiz, name='start_quiz'),  # expects ?role=role_id GET param
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),

    # Optional: additional role specific pages
    path('frontend/', views.frontend, name='frontend'),
    path('backend/', views.backend_view, name='backend'),
    path('data_scientist/', views.data_scientist_view, name='data_scientist'),
    path('cloud_engineer/', views.cloud_engineer, name='cloud_engineer'),

    path('aptitude/', views.aptitude_view, name='aptitude'),

]
