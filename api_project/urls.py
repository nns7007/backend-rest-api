from django.urls import path
from api_project import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
