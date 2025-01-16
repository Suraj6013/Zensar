from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=100)
    toppings = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.customer_name} - {self.pizza.name} - {self.quantity}"