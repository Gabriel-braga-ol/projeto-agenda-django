from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'), #sempre colocar uma / no final da url
    path('', views.index, name='index'),
]