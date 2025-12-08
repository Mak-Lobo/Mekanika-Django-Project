from django.contrib import admin
from django.urls import include, path
import Admin.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_service/', views.add_service, name='add_service'),
    path('add_service/delete/<int:pk>/', views.delete_service, name='delete_service'),
]