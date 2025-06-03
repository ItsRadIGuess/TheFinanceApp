from django.db import models

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"Income {self.amount} on {self.date}"

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"Expense {self.amount} on {self.date}"

class Asset(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Liability(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Annual interest rate as a percentage",
    )

    def projected_balance(self, years: int = 1):
        """Return balance projected with compound interest."""
        rate = self.interest_rate / 100
        return self.balance * (1 + rate) ** years

    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.CharField(max_length=100)
    shares = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dividend_yield = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Annual dividend yield as a percentage",
    )

    def current_value(self):
        return self.shares * self.price

    def annual_dividend(self):
        return self.current_value() * (self.dividend_yield / 100)

    def __str__(self):
        return self.name

