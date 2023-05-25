from django.contrib import admin
from django.urls import path
from Test import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('tests/', views.tests, name='alltests'),
    path('save-answers/', views.save_answers, name='save_answers'),
    path('tests/<int:id>',views.test, name='test'),
]
