from django.urls import path
from hapl import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("customers/", views.customers, name="customers"),
    path("contact/", views.contact, name="contact"),
    path("news/", views.news, name="news"),
    path("news/<str:article_id>/", views.article, name="article"),
    path("career/", views.career, name="career"),
]
