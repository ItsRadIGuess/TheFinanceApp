from decimal import Decimal

from django.test import TestCase

from .models import Asset, BankAccount, Liability, Stock
from .services import calculate_net_worth, total_dividends


class FinanceModelTests(TestCase):
    def setUp(self):
        Asset.objects.create(name="Car", value=Decimal("10000"))
        BankAccount.objects.create(name="Checking", balance=Decimal("5000"), interest_rate=Decimal("5"))
        Stock.objects.create(name="ACME", shares=10, price=Decimal("20"), dividend_yield=Decimal("2"))
        Liability.objects.create(name="Loan", amount=Decimal("3000"))

    def test_projected_balance(self):
        acct = BankAccount.objects.get(name="Checking")
        self.assertEqual(acct.projected_balance(), Decimal("5250"))

    def test_annual_dividend(self):
        stock = Stock.objects.get(name="ACME")
        self.assertEqual(stock.annual_dividend(), Decimal("4"))

    def test_calculate_net_worth(self):
        networth = calculate_net_worth()
        # Assets 10000 + projected bank balance 5250 + stock value 200 - liabilities 3000
        self.assertEqual(networth, Decimal("12450"))
        self.assertEqual(total_dividends(), Decimal("4"))
