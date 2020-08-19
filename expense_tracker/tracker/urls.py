from django.urls import path
from tracker.views import dashboard,get_all_wallet,delete_wallet,edit_wallet,create_wallet,get_all_expense,create_expense,edit_expense,delete_expense,get_all_income,create_income,delete_income,edit_income
urlpatterns = [
    path('dashboard/',dashboard),
    path('wallet/',get_all_wallet),
    path('create_wallet/',create_wallet),
    path('edit_wallet/<int:wallet_id>/',edit_wallet),
    path('delete_wallet/<int:wallet_id>/',delete_wallet),
    path('expense/',get_all_expense),
    path('create_expense/',create_expense),
    path('edit_expense/<int:expense_id>/',edit_expense),
    path('delete_expense/<int:expense_id>/',delete_expense),
    path('income/',get_all_income),
    path('create_income/',create_income),
    path('delete_income/<int:income_id>/',delete_income),
    path('edit_income/<int:income_id>/',edit_income),
]
