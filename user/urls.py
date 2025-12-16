from django.contrib import admin
from django.urls import include, path

from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.book_service, name='book'),
    path('feedback/', views.feedback_list, name='feedback_list'),
    path('feedback/submit/', views.submit_feedback, name='submit_feedback'),
]
