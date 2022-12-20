from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scraper-form/', views.index, name='scraper-form'),
    path('', views.redirect_view, name='redirect')
]