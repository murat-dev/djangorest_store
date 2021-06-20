from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileCustomerListView.as_view()),
    path('detail/<int:pk>/', ProfileCustomerDetailView.as_view()),
    path('update/<int:pk>/', ProfileCustomerUpdateView.as_view()),
]
