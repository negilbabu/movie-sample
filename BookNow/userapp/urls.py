from django.urls import path
from .views import UserView, LoginView

urlpatterns = [

    path('signup', UserView.as_view(), name="adduser"),
    path('login', LoginView.as_view(), name="login")

]
