from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework_jwt.views import ObtainJSONWebToken

from core.custom_jwt_serializer import CustomJWTSerializer

from project import settings


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^api/', include('users.api.routers')),
]

if settings.NSS_USE_JWT:
	urlpatterns += [
		url(r'^o/authorize/', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
	]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
