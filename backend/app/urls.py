
from django.contrib import admin
from django.urls import include, path
#views import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/asset/', include('app.api_urls.asset_urls')),    
    path('api/invplan/', include('app.api_urls.invplan_urls')),
    path('api/user/', include('app.api_urls.user_urls')),    
]
