"""universe URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "TAXALIAN ADVENTURER Admin"
admin.site.site_title = "TAXALIAN ADVENTURER Admin Portal"
admin.site.index_title = "Welcome to TAXALIAN ADVENTURER Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('index/',views.index,name='index'),
    path('services/',views.services,name='services'),
    path('packages/',views.packages,name='packages'),
    path('partner/',views.partner,name='partner'),
    path('participent/',views.participent,name='participent'),
    path('adventurer/',views.adventurer,name='adventurer'),
    path('prize_winner/',views.prize_winner,name='prize_winner'),
    path('invester/',views.invester,name='invester'),
    path('desired_area/',views.desired_area,name='desired_area'),
    path('training_learning/',views.training_learning,name='training_learning'),
    path('tasks/',views.tasks,name='tasks'),
    path('subcontact/',views.subcontact,name='subcontact'),
    path('earth/',include('earth.urls')),
    path('galaxy/',include('galaxy.urls')),
    path('jupiter/',include('jupiter.urls')),
    path('mars/',include('mars.urls')),
    path('sun/',include('sun.urls')),
    
    
    ] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


print(static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT))