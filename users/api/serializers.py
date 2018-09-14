from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import NSSReview


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'first_name', 'last_name']


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = NSSReview
		fields = ['user', 'course_name', 'description', 'note']
