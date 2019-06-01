from django.db import models
from django.conf import settings
# Create your models here.


class Category(models.Model):
   name = models.CharField(max_length=35)
def __str__(self):
   		return self.name


class Post(models.Model):
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL, null = True, on_delete=models.DO_NOTHING)
	title = models.CharField(max_length=50)
	body = models.TextField()
	published = models.DateTimeField(auto_now_add=True, null=True)

	Category = models.ForeignKey(Category,on_delete=models.CASCADE, 
								null=True)

	
def __str__(self):
	return "{} published by{} on{}".format(self.title, self.author, self.published)


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name = "comments", null=True, on_delete=models.DO_NOTHING)
	author = models.CharField(max_length =50)
	body = models.TextField()
	active = models.BooleanField(default=True)
	published = models.DateTimeField(auto_now_add=True)
	featured = models.BooleanField(default = True)







