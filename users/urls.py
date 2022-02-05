from django.urls import path,include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
router=routers.SimpleRouter()
router.register('users',views.UserView,basename='userview')

urlpatterns=[
    path('',include(router.urls)),
    # path('users/',views.UserView.as_view()),
    # path('users',views.UserView.as_view()),
]
            # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
