# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('receipt', models.CharField(max_length=13, db_index=True)),
                ('role', models.CharField(max_length=9, choices=[('VENDOR', 'Vendor'), ('AFFILIATE', 'Affiliate')])),
                ('transaction_type', models.CharField(max_length=15, choices=[('SALE', 'Sale'), ('BILL', 'Rebill'), ('RFND', 'Refund'), ('CGBK', 'Chargeback'), ('INSF', 'Insufficient Funds (eCheck)'), ('CANCEL-REBILL', 'Cancel Rebill'), ('UNCANCEL-REBILL', 'Resume Rebill'), ('TEST', 'IPN Test'), ('TEST_SALE', 'Test Sale'), ('TEST_BILL', 'Test Rebill'), ('TEST_RFND', 'Test Refund'), ('TEST_CHGBK', 'Test Chargeback')])),
                ('transaction_vendor', models.CharField(max_length=10, blank=True)),
                ('transaction_affiliate', models.CharField(null=True, max_length=10, blank=True)),
                ('recieved_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('order_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tax_amount', models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)),
                ('payment_method', models.CharField(null=True, max_length=4, blank=True, choices=[('PYPL', 'Paypal'), ('VISA', 'Visa'), ('MSTR', 'Mastercard'), ('DISC', 'Discover'), ('AMEX', 'American Express'), ('SWIT', 'Switch?'), ('SOLO', 'Solo'), ('JCBC', 'JCBC'), ('DNRS', 'Diners Club'), ('ENRT', 'ENRT'), ('AUST', 'AUST'), ('BLME', 'BLME'), ('STVA', 'STVA'), ('MAES', 'Maestro'), ('TEST', 'Test Credit Card')])),
                ('currency', models.CharField(max_length=3)),
                ('tracking_id', models.CharField(null=True, max_length=255, blank=True)),
                ('notification_version', models.CharField(null=True, max_length=5, blank=True)),
                ('extra_data', models.CharField(null=True, max_length=1024, blank=True)),
                ('transaction_date', models.DateTimeField()),
                ('sender_ip', models.IPAddressField(blank=True)),
                ('order_language', models.CharField(null=True, max_length=20, blank=True)),
                ('product_title', models.CharField(null=True, max_length=255, blank=True)),
                ('product_type', models.CharField(max_length=11, choices=[('STANDARD', 'Standard'), ('RECURRING', 'Recurring')])),
                ('product_id', models.CharField(max_length=5)),
                ('verification_passed', models.BooleanField(default=True)),
                ('parent_receipt', models.CharField(null=True, max_length=13, blank=True, db_index=True)),
                ('upsell_flow', models.CharField(null=True, max_length=20, blank=True)),
                ('rebill_amount', models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)),
                ('rebill_parent_receipt', models.CharField(null=True, max_length=13, blank=True, db_index=True)),
                ('processed_payments', models.IntegerField(null=True, blank=True)),
                ('future_payments', models.IntegerField(null=True, blank=True)),
                ('next_payment_date', models.DateField(null=True, blank=True)),
                ('rebill_status', models.CharField(null=True, max_length=10, blank=True, choices=[('ACTIVE', 'Active'), ('COMPLETED', 'Completed'), ('CANCELED', 'Cancelled')])),
                ('rebill_frequency', models.CharField(null=True, max_length=20, blank=True)),
                ('full_name', models.CharField(max_length=510)),
                ('first_name', models.CharField(null=True, max_length=255, blank=True)),
                ('last_name', models.CharField(null=True, max_length=255, blank=True)),
                ('province', models.CharField(null=True, max_length=255, blank=True)),
                ('postal_code', models.CharField(null=True, max_length=16, blank=True)),
                ('city', models.CharField(null=True, max_length=255, blank=True)),
                ('country', models.CharField(null=True, max_length=255, blank=True)),
                ('country_code', models.CharField(null=True, max_length=2, blank=True)),
                ('email', models.CharField(max_length=255)),
                ('address1', models.CharField(null=True, max_length=255, blank=True)),
                ('address2', models.CharField(null=True, max_length=255, blank=True)),
                ('shipping_address1', models.CharField(null=True, max_length=255, blank=True)),
                ('shipping_address2', models.CharField(null=True, max_length=255, blank=True)),
                ('shipping_city', models.CharField(null=True, max_length=255, blank=True)),
                ('shipping_county', models.CharField(null=True, max_length=255, blank=True)),
                ('shipping_province', models.CharField(null=True, max_length=255, blank=True)),
                ('shipping_postal_code', models.CharField(null=True, max_length=255, blank=True)),
                ('shipping_country', models.CharField(null=True, max_length=255, blank=True)),
                ('shipping_amount', models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('post_data', models.CharField(null=True, max_length=4096, blank=True)),
                ('get_data', models.CharField(null=True, max_length=4096, blank=True)),
                ('failed', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='notification',
            name='post_data',
            field=models.ForeignKey(blank=True, null=True, to='django_clickbank.Post'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='notification',
            unique_together=set([('receipt', 'transaction_type')]),
        ),
    ]
