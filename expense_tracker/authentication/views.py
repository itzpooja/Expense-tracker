from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		email = request.POST.get("email")

		user = User.objects.create_user(
				username=username,
				password=password,
				email=email
			)
		login(request, user)

		return redirect("/dashboard/")

	return render(request, "signup.html")


def signin(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(username=username, password=password)

		if user != None:
			login(request, user)
			return redirect("/dashboard/")

	return render(request, "signin.html")


def signout(request):
	logout(request)
	return redirect("/signin/")
