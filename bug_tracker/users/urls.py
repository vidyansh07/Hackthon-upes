from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, home

urlpatterns = [
    path('', home),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
