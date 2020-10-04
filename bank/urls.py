from django.urls import path
from .views import ClientAPI, ClientIntance, TransactionAccounAPI

urlpatterns = [
    path('clients/', ClientAPI.as_view()),
    path('clients/<int:pk>/', ClientIntance.as_view()),
    path('transaction/<uuid:pk>/', TransactionAccounAPI.as_view()),
]