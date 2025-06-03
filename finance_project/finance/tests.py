from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Asset, BankAccount, Liability, Stock
from .services import (
    calculate_net_worth,
    total_dividends,
    total_interest,
    total_passive_income,
)


class FinanceModelTests(TestCase):
    def setUp(self):
        Asset.objects.create(name="Car", value=Decimal("10000"))
        BankAccount.objects.create(name="Checking", balance=Decimal("5000"), interest_rate=Decimal("5"))
        Stock.objects.create(name="ACME", shares=10, price=Decimal("20"), dividend_yield=Decimal("2"))
        Liability.objects.create(
            name="Loan",
            amount=Decimal("3000"),
            payment_amount=Decimal("250"),
            payment_frequency="month",
            payments_remaining=12,
            interest_rate=Decimal("5"),
            notes="Car loan",
        )

    def test_projected_balance(self):
        acct = BankAccount.objects.get(name="Checking")
        self.assertEqual(acct.projected_balance(), Decimal("5250"))

    def test_annual_dividend(self):
        stock = Stock.objects.get(name="ACME")
        self.assertEqual(stock.annual_dividend(), Decimal("4"))

    def test_annual_interest(self):
        acct = BankAccount.objects.get(name="Checking")
        self.assertEqual(acct.annual_interest(), Decimal("250"))

    def test_calculate_net_worth(self):
        networth = calculate_net_worth()
        # Assets 10000 + projected bank balance 5250 + stock value 200 - liabilities 3000
        self.assertEqual(networth, Decimal("12450"))
        self.assertEqual(total_dividends(), Decimal("4"))
        self.assertEqual(total_interest(), Decimal("250"))
        self.assertEqual(total_passive_income(), Decimal("254"))


class FinanceViewTests(TestCase):
    def setUp(self):
        Asset.objects.create(name="Laptop", value=Decimal("1000"))
        BankAccount.objects.create(name="Savings", balance=Decimal("1500"), interest_rate=Decimal("2"))
        Stock.objects.create(name="XYZ", shares=5, price=Decimal("10"), dividend_yield=Decimal("1"))

    def test_asset_list_view(self):
        response = self.client.get(reverse("asset_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Laptop")
        self.assertContains(response, "Savings")
        self.assertContains(response, "XYZ")

    def test_dashboard_view_totals(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["asset_total"], Decimal("2550"))
        self.assertEqual(response.context["passive_income_total"], Decimal("30.50"))
