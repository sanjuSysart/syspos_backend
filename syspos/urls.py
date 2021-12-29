
from django.urls import path
from.views import LoginView,CreateCustomer,UpdateDeleteCustomer
urlpatterns = [
    path('log',LoginView.as_view()),
    path('add_customer',CreateCustomer.as_view()),
    path('editupdate_customer/<int:pk>',UpdateDeleteCustomer.as_view())
]
