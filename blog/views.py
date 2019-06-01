from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, Category
from .forms import commentForm , PostForm, LoginForm
from django.contrib.auth import authenticate,login
#from django.contrib.auth decorators import login_required

# Create your views here.
def homepage(request): 
	post = Post.objects.all()
	categories = Category.objects.all()
	header = "This is my Blog"
	#print(Post)


	return render(request, 'blog.html', {
		'title':post,
		'header':header,
		'category':categories,
		})

def singlepost(request, post_id):

	post = Post.objects.get(id=post_id)
	form = commentForm()
	comments = post.comments.all()


	if request.method =="POST":
		form = commentForm(request.POST)



	if form.is_valid:
		comment = form.save(commit=False)
		comment.post = post
		comment.author = request.user
		comment.save()


	comments = post.comments.all()


	return render (request,'singlepost.html', {'post':post, 'form':form, 'post':post,'form':form, 'comments':comments })


#@login_required
def create_post(request):

	create_post = PostForm()


	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('/blog')

 

	return render (request, 'create_post.html', {'new_post_form':create_post})



def about(request):
	return render (request, 'about.html', {})

#@login_required
def login_view(request):

	form = LoginForm()

	if request.method == "POST":

		form = LoginForm(request.POST)
		if form.is_valid():
			#form = LoginForm(request.POST)
			cd = form.cleaned_data()
			user = authenticate(username=cd['username'],password=cd['password'])
			#print(user)

		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('blog/')
				#return HttpResponse('Login Successful')
			else:
				#return HttpResponse('Disabled Account')
				form = LoginForm()

		else:
			#return HttpResponse('invalid Account')
			form = LoginForm()




	else: 
		form = LoginForm()
	return render(request, 'Login.html', {'form':form})



	
