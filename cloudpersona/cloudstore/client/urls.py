from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='client_register'),
    path('login/', views.login_view, name='client_login'),
    path('store/', views.redirect_to_store, name='client_store'),

]
