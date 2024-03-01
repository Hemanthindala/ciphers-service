from django.urls import path
from .views import *

urlpatterns = [
    path('', greetings),
    path('ceaser/<str:plain_text>/<int:shift>', encode),


]
