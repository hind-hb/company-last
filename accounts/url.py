from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
              path('signup/', views.signup, name="signup"),
              path('login/',views.LoginView.as_view(template_name='login.html'),name='login'),
              path('logout/', auth_views.LogoutView.as_view(), name='logout'),



]