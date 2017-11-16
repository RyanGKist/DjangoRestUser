from __future__ import unicode_literals

from django.db import models

class BlogManager(models.Manager):
	def basic_validation(self, postData):
		errors = {}
		if len(postData['name']) < 1:
			errors['name'] = "Please add name!"
		if len(postData['email']) <1:
			errors['email'] = "Please add email!"
		return errors

class User(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = BlogManager()

# Create your models here.
