from django import forms
from .models import Comment, Category, Post

class commentForm(forms.ModelForm):


	  class Meta:
	  	model = Comment
	  	fields = ('author','body', )

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', 'Category')


class LoginForm(forms.Form):
	
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class EmailPostForm(forms.Form):
	name= forms.CharField(max_length=25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False, widget=forms.Textarea)

