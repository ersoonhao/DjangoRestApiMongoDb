"""DjangoRestApiMongoDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include , re_path
# from django.conf.urls import url



# from tutorials import views


#URL IS DEPRECIATED https://stackoverflow.com/questions/70319606/importerror-cannot-import-name-url-from-django-conf-urls-after-upgrading-to
# root url routing config file 

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/tutorials/', views.tutorial_list),
    # url(r'^', include('tutorials.urls')),
    re_path(r'^', include('tutorials.urls')),
]
