from django.urls import path
from hapl import views

urlpatterns = [
    path("", views.index, name="home"),
]
