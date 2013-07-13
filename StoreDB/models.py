from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateField()


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    signup_date = models.DateField()
    current_cart_contents = models.ManyToManyField(Product)


class Purchase(models.Model):
    customer_id = models.ForeignKey(Customer)
    product_id = models.ForeignKey(Product)
    date = models.DateField()
    fulfilled = models.BooleanField()


class Subscriptions(models.Model):
    customer_id = models.ForeignKey(Customer)
    product_id = models.ForeignKey(Product)
    init_date = models.DateField()
    frequency = models.IntegerField()  # number of days between deliveries
    quantity = models.IntegerField()   # number of items / delivery
    next_delivery = models.DateField()
