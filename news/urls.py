from django.urls import path
from news import views

namespace = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
]