from decimal import Decimal

from .models import Asset, BankAccount, Liability, Stock


def calculate_net_worth(years: int = 1) -> Decimal:
    """Return projected net worth using assets, bank accounts and stocks."""
    asset_total = sum(a.value for a in Asset.objects.all())
    bank_total = sum(ba.projected_balance(years) for ba in BankAccount.objects.all())
    stock_total = sum(s.current_value() for s in Stock.objects.all())
    liability_total = sum(l.amount for l in Liability.objects.all())
    return asset_total + bank_total + stock_total - liability_total


def total_dividends() -> Decimal:
    """Return total annual dividends from all stocks."""
    return sum(s.annual_dividend() for s in Stock.objects.all())


def total_interest() -> Decimal:
    """Return total annual interest from all bank accounts."""
    return sum(acct.annual_interest() for acct in BankAccount.objects.all())


def total_passive_income() -> Decimal:
    """Return combined dividends and interest."""
    return total_dividends() + total_interest()

