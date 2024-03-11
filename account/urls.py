from django.urls import path
from .views import UserRegistrationView, UserLoginView


app_name = 'account'
urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
]
