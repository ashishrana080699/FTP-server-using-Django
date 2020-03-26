from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('info', views.info, name='info'),
    path('find', views.find, name='find'),
    path('search', views.search, name='search'),
   path('info_upload', views.info_upload, name='info_upload'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)