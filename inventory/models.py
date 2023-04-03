from django.db import models

# Create your models here.

class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    remark = models.TextField(blank=True)
    remark1 = models.TextField(blank=True)
    
def __str__(self):
    return self.name

# модель для товаров
# class Product(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
        
    
    # сделать связь с моделью склада
    # сделать связь с моделью компании
    # сделать связь с моделью категории