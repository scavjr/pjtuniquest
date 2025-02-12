from django.urls import path
from apphome import views

urlpatterns = [
  
        path("", views.home, name="home"),
        path("logout", views.logout_view, name="homelogout"),
        
       ]
