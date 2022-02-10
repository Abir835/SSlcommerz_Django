
from django.urls import path
from sslcommerz import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ssl/status/', views.ssl_status, name='ssl_status'),
    path('ssl/complete/<val_id>/<tran_id>/', views.ssl_complate, name='ssl_complete'),
]