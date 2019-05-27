from django.db import models


class Customer(models.Model):
    first_name = models.CharField(blank=True, max_length=255)
    last_name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Phone(models.Model):
    number = models.CharField(max_length=32)
    customer = models.ForeignKey('Customer', related_name='phones', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('customer', 'number')

    def __str__(self):
        return self.number


class Email(models.Model):
    address = models.EmailField()
    customer = models.ForeignKey('Customer', related_name='emails', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('customer', 'address')

    def __str__(self):
        return self.address
