from django.shortcuts import render,redirect
from tracker.models import Wallet,Expense,Income
from datetime import datetime

def dashboard(request):
	all_wallet=Wallet.objects.all()
	all_expense=Expense.objects.all()
	all_income=Income.objects.all()
	return render(request,"dashboard.html",{"all_wallet":all_wallet,"all_expense":all_expense,"all_income":all_income})

# Create your views here.
def get_all_wallet(request):
	user= request.user
	all_wallet=Wallet.objects.all()
	return render(request,"wallet.html",{"all_wallet":all_wallet})

def create_wallet(request):
	if request.method == "POST":
		wallet_name = request.POST["name"]
		wallet_balance = request.POST["balance"]

		wallet_object = Wallet.objects.create(
			name = wallet_name,
			balance = wallet_balance,
			last_transaction = datetime.now(),
			user = request.user
			)
		return redirect("/wallet/")
	return redirect("/wallet/")

def delete_wallet(request, wallet_id):
	wallet_object = Wallet.objects.get(pk=wallet_id)
	wallet_object.delete()

	return redirect("/wallet/")

def edit_wallet(request, wallet_id):
	wallet_object = Wallet.objects.get(pk=wallet_id)

	if request.method == "POST":
		wallet_name = request.POST["name"]
		wallet_balance = request.POST["balance"]
		print("heyy")
		wallet_object = Wallet.objects.get(pk=wallet_id)
		wallet_object.name = wallet_name
		wallet_object.balance = wallet_balance
		wallet_object.last_transaction = datetime.now()

		wallet_object.save()
		return redirect("/wallet/")

	return render(request, "edit_wallet.html", {"wallet_object":wallet_object})


def get_all_expense(request):
	user= request.user
	all_expense=Expense.objects.all()
	all_wallet=Wallet.objects.all()
	return render(request,"expense.html",{"all_expense":all_expense,"all_wallet":all_wallet})


def create_expense(request):
	if request.method == "POST":
		wallet_id = request.POST["wallet"]
		expense_title = request.POST["title"]
		expense_amount = request.POST["amount"]
		expense_description = request.POST["description"]
		wallet_object = Wallet.objects.get(pk=wallet_id)
		expense_object = Expense.objects.create(
			title = expense_title,
			amount = expense_amount,
			description = expense_description,
			timestamp = datetime.now(),
			user = request.user,
			wallet = wallet_object
			)

		wallet_object.balance -= int(expense_amount)
		wallet_object.save()

		return redirect("/expense/")

	return redirect("/expense/")


def delete_expense(request, expense_id):
	expense_object = Expense.objects.get(pk=expense_id)
	expense_object.delete()

	return redirect("/expense/")


def edit_expense(request, expense_id):
	expense_object = Expense.objects.get(pk=expense_id)

	if request.method == "POST":
		expense_title = request.POST["title"]
		expense_amount = request.POST["amount"]
		expense_description = request.POST["description"]
		expense_object = Expense.objects.get(pk=expense_id)
		expense_object.title = expense_title
		expense_object.amount = expense_amount
		expense_object.description = expense_description
		expense_object.timestamp = datetime.now()

		expense_object.save()

		return redirect("/expense/")

	return render(request, "edit_expense.html", {"expense":expense_object})


def get_all_income(request):
    user = request.user
    all_wallet = Wallet.objects.filter(user=user)
    all_income = Income.objects.filter(user=user)
    return render(request, "income.html", {"all_wallet":all_wallet, "all_income":all_income})


def create_income(request):
	if request.method == "POST":
		wallet_id = request.POST["wallet"]
		income_title = request.POST["title"]
		income_amount = request.POST["amount"]
		income_description = request.POST["description"]

		wallet_instance = Wallet.objects.get(pk=wallet_id)

		income_instance = Income.objects.create(
			title = income_title,
			amount = income_amount,
			description = income_description,
			timestamp = datetime.now(),
			user = request.user,
			wallet = wallet_instance
			)

		wallet_instance.balance += int(income_amount)
		wallet_instance.save()

		return redirect("/income/")

	return redirect("/income/")


def delete_income(request, income_id):
	income_object = Income.objects.get(pk=income_id)
	income_object.delete()

	return redirect("/income/")

def edit_income(request, income_id):
	income_object = Income.objects.get(pk=income_id)

	if request.method == "POST":
		income_title = request.POST["title"]
		income_amount = request.POST["amount"]
		income_description = request.POST["description"]

		income_object = Income.objects.get(pk=income_id)

		income_object.title = income_title
		income_object.amount = income_amount
		income_object.description = income_description
		income_object.timestamp = datetime.now()

		income_object.save()

		return redirect("/income/")

	return render(request, "edit_income.html", {"income":income_object})