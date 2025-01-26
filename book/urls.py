from django.urls import path
from . import views

urlpatterns = [
    path('', views.guestbook_view, name='guestbook'),
]
