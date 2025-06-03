from django.urls import path
from . import views

urlpatterns = [
    path('income/', views.IncomeList.as_view(), name='income_list'),
    path('income/<int:pk>/', views.IncomeDetail.as_view(), name='income_detail'),
    path('income/add/', views.IncomeCreate.as_view(), name='income_add'),
    path('income/<int:pk>/edit/', views.IncomeUpdate.as_view(), name='income_edit'),
    path('income/<int:pk>/delete/', views.IncomeDelete.as_view(), name='income_delete'),

    path('expense/', views.ExpenseList.as_view(), name='expense_list'),
    path('expense/<int:pk>/', views.ExpenseDetail.as_view(), name='expense_detail'),
    path('expense/add/', views.ExpenseCreate.as_view(), name='expense_add'),
    path('expense/<int:pk>/edit/', views.ExpenseUpdate.as_view(), name='expense_edit'),
    path('expense/<int:pk>/delete/', views.ExpenseDelete.as_view(), name='expense_delete'),

    path('asset/', views.AssetList.as_view(), name='asset_list'),
    path('asset/<int:pk>/', views.AssetDetail.as_view(), name='asset_detail'),
    path('asset/add/', views.AssetCreate.as_view(), name='asset_add'),
    path('asset/<int:pk>/edit/', views.AssetUpdate.as_view(), name='asset_edit'),
    path('asset/<int:pk>/delete/', views.AssetDelete.as_view(), name='asset_delete'),

    path('liability/', views.LiabilityList.as_view(), name='liability_list'),
    path('liability/<int:pk>/', views.LiabilityDetail.as_view(), name='liability_detail'),
    path('liability/add/', views.LiabilityCreate.as_view(), name='liability_add'),
    path('liability/<int:pk>/edit/', views.LiabilityUpdate.as_view(), name='liability_edit'),
    path('liability/<int:pk>/delete/', views.LiabilityDelete.as_view(), name='liability_delete'),

    path('bankaccount/', views.BankAccountList.as_view(), name='bankaccount_list'),
    path('bankaccount/<int:pk>/', views.BankAccountDetail.as_view(), name='bankaccount_detail'),
    path('bankaccount/add/', views.BankAccountCreate.as_view(), name='bankaccount_add'),
    path('bankaccount/<int:pk>/edit/', views.BankAccountUpdate.as_view(), name='bankaccount_edit'),
    path('bankaccount/<int:pk>/delete/', views.BankAccountDelete.as_view(), name='bankaccount_delete'),

    path('stock/', views.StockList.as_view(), name='stock_list'),
    path('stock/<int:pk>/', views.StockDetail.as_view(), name='stock_detail'),
    path('stock/add/', views.StockCreate.as_view(), name='stock_add'),
    path('stock/<int:pk>/edit/', views.StockUpdate.as_view(), name='stock_edit'),
    path('stock/<int:pk>/delete/', views.StockDelete.as_view(), name='stock_delete'),
]
