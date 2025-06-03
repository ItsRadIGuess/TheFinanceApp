from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.db.models import Sum
from django.db.models.functions import TruncMonth


class ModelNameMixin:
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context

from .models import Income, Expense, Asset, Liability, BankAccount, Stock

# Dashboard view aggregates all financial information and shows monthly
# projections based on Income and Expense records.
class DashboardView(TemplateView):
    template_name = 'finance/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['income_total'] = (
            Income.objects.aggregate(total=Sum('amount'))['total'] or 0
        )
        context['expense_total'] = (
            Expense.objects.aggregate(total=Sum('amount'))['total'] or 0
        )
        context['asset_total'] = (
            Asset.objects.aggregate(total=Sum('value'))['total'] or 0
        )
        context['liability_total'] = (
            Liability.objects.aggregate(total=Sum('amount'))['total'] or 0
        )

        income_months = (
            Income.objects
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(total=Sum('amount'))
            .order_by('month')
        )
        expense_months = (
            Expense.objects
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(total=Sum('amount'))
            .order_by('month')
        )
        context['income_by_month'] = income_months
        context['expense_by_month'] = expense_months
        return context

# Income views
class IncomeList(ModelNameMixin, ListView):
    model = Income
    template_name = 'finance/list.html'

class IncomeDetail(ModelNameMixin, DetailView):
    model = Income
    template_name = 'finance/detail.html'

class IncomeCreate(ModelNameMixin, CreateView):
    model = Income
    fields = ['amount', 'description', 'date']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('income_list')

class IncomeUpdate(ModelNameMixin, UpdateView):
    model = Income
    fields = ['amount', 'description', 'date']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('income_list')

class IncomeDelete(ModelNameMixin, DeleteView):
    model = Income
    template_name = 'finance/confirm_delete.html'
    success_url = reverse_lazy('income_list')

# Expense views
class ExpenseList(ModelNameMixin, ListView):
    model = Expense
    template_name = 'finance/list.html'

class ExpenseDetail(ModelNameMixin, DetailView):
    model = Expense
    template_name = 'finance/detail.html'

class ExpenseCreate(ModelNameMixin, CreateView):
    model = Expense
    fields = ['amount', 'description', 'date']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('expense_list')

class ExpenseUpdate(ModelNameMixin, UpdateView):
    model = Expense
    fields = ['amount', 'description', 'date']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('expense_list')

class ExpenseDelete(ModelNameMixin, DeleteView):
    model = Expense
    template_name = 'finance/confirm_delete.html'
    success_url = reverse_lazy('expense_list')

# Asset views
class AssetList(ModelNameMixin, ListView):
    model = Asset
    template_name = 'finance/list.html'

class AssetDetail(ModelNameMixin, DetailView):
    model = Asset
    template_name = 'finance/detail.html'

class AssetCreate(ModelNameMixin, CreateView):
    model = Asset
    fields = ['name', 'value']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('asset_list')

class AssetUpdate(ModelNameMixin, UpdateView):
    model = Asset
    fields = ['name', 'value']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('asset_list')

class AssetDelete(ModelNameMixin, DeleteView):
    model = Asset
    template_name = 'finance/confirm_delete.html'
    success_url = reverse_lazy('asset_list')

# Liability views
class LiabilityList(ModelNameMixin, ListView):
    model = Liability
    template_name = 'finance/list.html'

class LiabilityDetail(ModelNameMixin, DetailView):
    model = Liability
    template_name = 'finance/detail.html'

class LiabilityCreate(ModelNameMixin, CreateView):
    model = Liability
    fields = [
        'name',
        'amount',
        'payment_amount',
        'payment_frequency',
        'payments_remaining',
        'interest_rate',
        'notes',
    ]
    template_name = 'finance/form.html'
    success_url = reverse_lazy('liability_list')

class LiabilityUpdate(ModelNameMixin, UpdateView):
    model = Liability
    fields = [
        'name',
        'amount',
        'payment_amount',
        'payment_frequency',
        'payments_remaining',
        'interest_rate',
        'notes',
    ]
    template_name = 'finance/form.html'
    success_url = reverse_lazy('liability_list')

class LiabilityDelete(ModelNameMixin, DeleteView):
    model = Liability
    template_name = 'finance/confirm_delete.html'
    success_url = reverse_lazy('liability_list')

# BankAccount views
class BankAccountList(ModelNameMixin, ListView):
    model = BankAccount
    template_name = 'finance/list.html'


class BankAccountDetail(ModelNameMixin, DetailView):
    model = BankAccount
    template_name = 'finance/detail.html'


class BankAccountCreate(ModelNameMixin, CreateView):
    model = BankAccount
    fields = ['name', 'balance', 'interest_rate']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('bankaccount_list')


class BankAccountUpdate(ModelNameMixin, UpdateView):
    model = BankAccount
    fields = ['name', 'balance', 'interest_rate']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('bankaccount_list')


class BankAccountDelete(ModelNameMixin, DeleteView):
    model = BankAccount
    template_name = 'finance/confirm_delete.html'
    success_url = reverse_lazy('bankaccount_list')


# Stock views
class StockList(ModelNameMixin, ListView):
    model = Stock
    template_name = 'finance/list.html'


class StockDetail(ModelNameMixin, DetailView):
    model = Stock
    template_name = 'finance/detail.html'


class StockCreate(ModelNameMixin, CreateView):
    model = Stock
    fields = ['name', 'shares', 'price', 'dividend_yield']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('stock_list')


class StockUpdate(ModelNameMixin, UpdateView):
    model = Stock
    fields = ['name', 'shares', 'price', 'dividend_yield']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('stock_list')


class StockDelete(ModelNameMixin, DeleteView):
    model = Stock
    template_name = 'finance/confirm_delete.html'
    success_url = reverse_lazy('stock_list')
