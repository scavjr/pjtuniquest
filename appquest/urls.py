from django.urls import path
from appquest import views


urlpatterns = [
    path("formquestions", views.verQuestao, name="formquestion"),
]
