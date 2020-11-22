"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from corona.presentation_layer.views.index_view import IndexView
from corona.presentation_layer.views.register_patient_view import RegisterPatientView
from corona.presentation_layer.views.doctor_view import DoctorView
from django.contrib.admin.views.decorators import staff_member_required
from corona.presentation_layer.views.logout_view import LogoutView
from corona.presentation_layer.views.doctor_login import DoctorLoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # include('corona.urls')
    path('register/', RegisterPatientView.as_view(), name='register'),
    path('doctor-login/', DoctorLoginView.as_view(), name='doctor-login'),
    path('admin/', admin.site.urls),
    path('doctor/', staff_member_required(DoctorView.as_view(), login_url='/doctor-login'), name='doctor'),
    path('logout/', LogoutView.as_view(), name='logout')
]
