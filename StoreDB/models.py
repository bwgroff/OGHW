from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000) # product description
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateField()

    def __unicode__(self):
        return self.name


class Customer(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    signup_date = models.DateField()
    current_cart_contents = models.ManyToManyField(Product)

    def __unicode__(self):
        return u'%s, %s' % (self.last_name, self.first_name)


class Purchase(models.Model):
    customer_id = models.ForeignKey(Customer)
    product_id = models.ForeignKey(Product)
    order_date = models.DateField()
    fulfilled = models.BooleanField()

    def __unicode__(self):
        return u'%s, %s' % (self.customer_id, self.order_date)


class Subscriptions(models.Model):
    customer_id = models.ForeignKey(Customer)
    product_id = models.ForeignKey(Product)
    init_date = models.DateField()
    frequency = models.IntegerField()  # number of days between deliveries
    quantity = models.IntegerField()   # number of items / delivery
    next_delivery = models.DateField()

    def __unicode__(self):
        return u'%s, %s' % (self.customer_id, self.init_date)
