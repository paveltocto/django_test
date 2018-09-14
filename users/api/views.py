from django.contrib.auth.models import User
from core.base_api_views import BaseModelSetView
from core.models import NSSReview
from users.api.serializers import UserSerializer, ReviewSerializer


class UserViewSet(BaseModelSetView):
	http_method_names = ['get', 'post']
	queryset = User.objects.all()
	serializer_class = UserSerializer


class ReviewViewSet(BaseModelSetView):
	http_method_names = ['get', 'post']
	queryset = NSSReview.objects.all()
	serializer_class = ReviewSerializer
