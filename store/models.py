from django.db import models
from django.contrib import admin
import datetime
from datetime import date
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Dealer(models.Model):
    d_ID = models.CharField(max_length=10, primary_key=True, default=0)
    d_name = models.CharField(max_length=20, default=0)
    d_phone = models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.d_ID

class Material(models.Model):
    m_ID = models.CharField(max_length=10, primary_key=True)  # 物料ID
    m_name = models.CharField(max_length=20, default=0)  # 物料名稱
    m_inventory = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    m_price = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    m_date = models.DateField(default=datetime.today())  # 進貨時間
    m_hcost = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    m_estsupply = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    m_estdemand = models.DecimalField(max_digits=8, decimal_places=0, default=0)

    def __str__(self):
        return self.m_ID

class Product(models.Model):
    p_ID = models.CharField(max_length=10, primary_key=True)
    p_name = models.CharField(max_length=20, default=0)
    p_price = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    p_inventory = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    p_cost = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    p_hcost = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    p_estsupply = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    p_estdemand = models.DecimalField(max_digits=8, decimal_places=0, default=0)

    def __str__(self):
        return self.p_ID

class Order(models.Model):
    o_ID = models.CharField(max_length=30, primary_key=True)
    o_amount = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    o_price = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    o_profit = models.DecimalField(max_digits=8, decimal_places=0, default=100)
    d_ID = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    p_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    o_date = models.DateField(default=date.today)

    def __str__(self):
        return self.o_ID

class Supplier(models.Model):
    s_ID = models.CharField(max_length=10, primary_key=True)
    s_name = models.CharField(max_length=20, default=0)
    s_phone = models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.s_ID

class Consume(models.Model):
    H_quantity = models.DecimalField(max_digits=8, decimal_places=0)
    o_ID = models.ForeignKey(Order, on_delete=models.CASCADE)
    p_ID = models.ForeignKey(Product, on_delete=models.CASCADE)


class Use(models.Model):
    U_quantity = models.DecimalField(max_digits=8, decimal_places=0)
    m_ID = models.ForeignKey(Material, on_delete=models.CASCADE)
    p_ID = models.ForeignKey(Product, on_delete=models.CASCADE)


class Retention(models.Model):
    Period = models.DecimalField(max_digits=3, decimal_places=0, primary_key=True)
    Retention = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    Survival = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    Active_Customers = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    Active_Periods = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    def __int__(self):
        return self.Period