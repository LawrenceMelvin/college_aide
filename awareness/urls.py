from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('aware/',views.aware,name='aware'),
    path('all/',views.all,name='all'),
    path('code/',views.all,name='code'),
    path('placement/',views.all,name='placement'),
    path('english/',views.all,name='english'),
    path('job/',views.all,name='job'),
]
