from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
	name = models.CharField(max_length=100)
	balance = models.IntegerField()
	last_transaction = models.DateTimeField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name

class Expense(models.Model):
	title = models.CharField(max_length=100)
	amount = models.IntegerField()
	timestamp = models.DateTimeField()
	description = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title

class Income(models.Model):
        title = models.CharField(max_length=100)
        
        amount = models.IntegerField()
        timestamp = models.DateTimeField()
        description = models.TextField()
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
        wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, null=True)
	
        def __str__(self):
                return self.title