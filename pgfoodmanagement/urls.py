"""pgfoodmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from foodmanageapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view),
    url(r'^signup/', views.registration_view),
    url(r'^menu/', views.menu_view),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/', views.logout_view),
    url(r'^p_info/', views.personal_info_view),
    url(r'^booked_members/', views.booked_members_view),
    url(r'^breakfast/', views.breakfast_view),
    url(r'^lunch/', views.lunch_view),
    url(r'^dinner/', views.dinner_view),
    url(r'^update/(?P<id>\d+)/$', views.update_view),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
