from django.urls import path
from nibal import views

urlpatterns = [
    path('',views.index,name='index')
]
