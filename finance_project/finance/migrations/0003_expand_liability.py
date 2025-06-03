from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_bankaccount_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='liability',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Regular payment amount', max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='liability',
            name='payment_frequency',
            field=models.CharField(choices=[('week', 'Weekly'), ('month', 'Monthly'), ('year', 'Yearly')], default='month', max_length=10),
        ),
        migrations.AddField(
            model_name='liability',
            name='payments_remaining',
            field=models.PositiveIntegerField(blank=True, help_text='Number of payments left', null=True),
        ),
        migrations.AddField(
            model_name='liability',
            name='interest_rate',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Annual interest rate as a percentage', max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='liability',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
