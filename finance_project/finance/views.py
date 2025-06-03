from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


class ModelNameMixin:
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context

from .models import Income, Expense, Asset, Liability

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
    fields = ['name', 'amount']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('liability_list')

class LiabilityUpdate(ModelNameMixin, UpdateView):
    model = Liability
    fields = ['name', 'amount']
    template_name = 'finance/form.html'
    success_url = reverse_lazy('liability_list')

class LiabilityDelete(ModelNameMixin, DeleteView):
    model = Liability
    template_name = 'finance/confirm_delete.html'
    success_url = reverse_lazy('liability_list')
