from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('match/', views.match, name="match"),
    path('about/', views.about, name="about"),
    path('chat/', views.chat, name="chat"),
    path('chatbot-response/', views.chatbot_response, name='chatbot_response'),

]