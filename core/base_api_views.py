from project import settings
from rest_framework import viewsets, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

_authentication_classes = []
_permission_classes = [permissions.IsAuthenticated]

if settings.NSS_USE_JWT:
	_authentication_classes.append(JSONWebTokenAuthentication)

_authentication_classes = tuple(_authentication_classes)


class BaseModelSetView(viewsets.ModelViewSet):
	authentication_classes = _authentication_classes
	permission_classes = _permission_classes
