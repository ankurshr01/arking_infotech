from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from AllInOne.forms import RegisterForm
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded


def Home(request):
	return render(request, 'AllInOne/home.html', )

def SignUp(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'AllInOne/home.html')
	else:
		form = RegisterForm()
	return render(request, 'AllInOne/signup.html', {'form': form})

def Login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return render(request, 'AllInOne/home.html')
	else:
		form = AuthenticationForm()
	return render(request, 'AllInOne/login.html', {'form':form})

def Logout(request):
	if request.method == 'POST':
		logout(request)
		return render(request, 'AllInOne/home.html')


@login_required(login_url="/AllInOne/Login/")
def ChangePassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect('/AllInOne/')

	else:
		form = PasswordChangeForm(request.user)

	
	return render(request, 'AllInOne/changepassword.html', {'form':form})


# Create your views here.







