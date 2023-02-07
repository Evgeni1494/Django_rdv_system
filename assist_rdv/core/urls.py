from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . views import logoutUser
from django.contrib.auth import logout



app_name = 'core'

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/',views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', views.logoutUser, name='logout')
]








