from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateField()

    def __unicode__(self):
        return self.name


class PurchaseRecord(models.Model):
    user_id = models.IntegerField()
    product_id = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()
    order_date = models.DateField()
    bill = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField()
    fulfilled = models.BooleanField()

    def __unicode__(self):
        return u'%s, %s' % (self.user_id, self.order_date)
