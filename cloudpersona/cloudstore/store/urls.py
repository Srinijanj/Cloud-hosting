from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registered_users/', views.registered_users, name='registered_users'),
    path('add_product/', views.add_product, name='add_product'),
    path('store/', views.store, name='store'),
    path('api/', include(router.urls)),
    path('', views.store_home, name='store_home'),
]
