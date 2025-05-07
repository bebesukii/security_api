#urls.py
from django.contrib import admin
from django.urls import path, include
from ..api.views import GoogleDorkSearchView

ROOT_URLCONF = 'security_api.urls'
urlpatterns = [
 
    path('google-dorks/', GoogleDorkSearchView.as_view(), name='google_dorks_search'),
    path('admin/', admin.site.urls),
    path('', include('security_api.urls')),  
]



