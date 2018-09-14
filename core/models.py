from django.contrib.auth.models import User
from django.db import models


class NSSReview(models.Model):
	user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE, related_name='user_reviews')
	course_name = models.CharField(max_length=127, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	note = models.FloatField(default=0)

	class Meta:
		db_table = 'fs_review'
