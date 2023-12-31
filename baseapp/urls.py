"""
URL configuration for pawsome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from baseapp import views

urlpatterns = [
    path('', views.website, name='website'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('help/',views.help,name='help'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='register'),
    



]
