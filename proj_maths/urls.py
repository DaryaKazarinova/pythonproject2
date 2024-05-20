'''urls'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('terms-list', views.terms_list),
    path('facts-list', views.facts_list),
    path('feedback-list', views.feedback_list),
    path('add-feedback', views.add_feedback),
    path('add-user', views.add_user),
    path('send-feedback', views.send_feedback),
    path('send-user', views.send_user)
]
