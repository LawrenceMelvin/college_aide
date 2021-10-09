from django.urls import path
from . import views
urlpatterns = [
    path('',views.note,name='home_note')
]