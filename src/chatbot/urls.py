from django.urls import path
from .views import chatbot_temp,chatbot

urlpatterns = [
    path('chatbot/',chatbot_temp,name='chatbot-temp'),
    path('chatbot/logic/',chatbot,name='chatbot'),
]
