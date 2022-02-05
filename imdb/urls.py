from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
# router.register('')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('users/',include('users.urls')),
    url('movies/',include('movies.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)