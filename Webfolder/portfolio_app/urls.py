from django.urls import path

from portfolio_app import views

urlpatterns = [
    path('', views.portfolio_app, name = "portfolio_app"),
    path('contact/', views.contact, name = "contact")
]