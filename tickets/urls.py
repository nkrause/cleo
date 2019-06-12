from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tickets import views

urlpatterns = [
    path('', views.api_root),
    path('login/', views.login),
    path('tickets/', views.ticket_list),
    path('ticket/<int:pk>/', views.ticket_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)