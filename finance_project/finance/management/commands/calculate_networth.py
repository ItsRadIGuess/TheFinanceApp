from django.core.management.base import BaseCommand

from ...services import calculate_net_worth, total_dividends
from ...models import BankAccount, Stock


class Command(BaseCommand):
    help = "Calculate projected balances, dividends and net worth"

    def handle(self, *args, **options):
        self.stdout.write("Projected Bank Account Balances:")
        for acct in BankAccount.objects.all():
            self.stdout.write(f"- {acct.name}: {acct.projected_balance():.2f}")

        self.stdout.write("\nExpected Annual Dividends:")
        for stock in Stock.objects.all():
            self.stdout.write(f"- {stock.name}: {stock.annual_dividend():.2f}")

        networth = calculate_net_worth()
        dividends = total_dividends()
        self.stdout.write(f"\nTotal Projected Net Worth: {networth:.2f}")
        self.stdout.write(f"Total Annual Dividends: {dividends:.2f}")

