
from django.urls import path
from appusers import views


urlpatterns = [

    path("cadastro_users", views.cad_usuario, name="cadastro"),
   
    
]
