"""django_chirper URL Configuration

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
import debug_toolbar
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.forms import LoginForm



urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)), 
    path('admin/', admin.site.urls),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name = 'login.html', 
            authentication_form = LoginForm
        ), 
        name = 'login'
    ),
    path(
        'logout/', 
        auth_views.LogoutView.as_view(
            template_name = 'logout.html'
        ), 
        name = 'logout'
    ),
    path('', include('main.urls')),
    path('', include('message.urls')),
    path('', include('blog.urls')),
    path('', include('user.urls')),
    path('account/', include('password_reset.urls')),
    path('settings/', include('user_settings.urls')),
    path('<str:handle>/', include('user_profile.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)