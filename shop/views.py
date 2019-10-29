from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

""" ***********     Home Page      ******** """

def index(request):
	return render(request, 'shop/index.html')


""" ***********     Contact Form for website visitors      ******** """

def contact(request):
	if request.method == "POST":
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		phone = request.POST.get('phone', '')
		desc = request.POST.get('desc', '')
		contact = Contact(user_name=name, user_email=email, user_phone=phone, user_desc=desc)
		contact.save()
	return render(request, 'shop/contact.html')


""" ***********     User Signup      ******** """

def signup(request):
	if request.method == 'POST':
		if request.POST['password1']== request.POST['password2']:
			try: 
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'shop/signup.html', {'usernameerror':'username is already exist please try a different name'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				auth.login(request, user)
				return redirect('index')
		else:
			return render(request, 'shop/signup.html', {'passworderror': 'password does not matched'})
	else:
		return render(request, 'shop/signup.html')


	return render(request, 'shop/signup.html')


""" ***********     User Login      ***********     """

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('index')
		else:
			return render(request, 'shop/login.html', {'error':'username or password is incorrect'})
	else:
		return render(request, 'shop/login.html')


""" Logout function """
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('index')



""" ***********     There are three blogs      ******** """
def evening_walk(request):
	return render(request, 'shop/evening_walk.html')

def zymjoin(request):
	return render(request, 'shop/zymjoin.html')

def junkfood(request):
	return render(request, 'shop/junkfood.html')
