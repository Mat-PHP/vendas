from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class Sale(models.Model):
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    @property
    def total(self):
        return self.quantity * self.price
    def __str__(self):
        return f"{self.product} - {self.date}"
