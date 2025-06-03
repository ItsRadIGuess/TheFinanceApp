from django.db import models

class Income(models.Model):
    """Recurring income entry."""

    FREQUENCY_CHOICES = [
        ("W", "Weekly"),
        ("M", "Monthly"),
        ("Y", "Yearly"),
    ]

    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=1, choices=FREQUENCY_CHOICES)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name} {self.amount} ({self.get_frequency_display()})"

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
    payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Regular payment amount",
    )
    PAYMENT_FREQUENCY_CHOICES = [
        ("week", "Weekly"),
        ("month", "Monthly"),
        ("year", "Yearly"),
    ]
    payment_frequency = models.CharField(
        max_length=10,
        choices=PAYMENT_FREQUENCY_CHOICES,
        default="month",
    )
    payments_remaining = models.PositiveIntegerField(
        null=True, blank=True, help_text="Number of payments left"
    )
    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Annual interest rate as a percentage",
    )
    notes = models.TextField(blank=True)

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

