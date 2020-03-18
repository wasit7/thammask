from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)

class Review(models.Model):
    receive = models.OneToOneField(Receive, on_delete=models.CASCADE)
    score = models.IntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    thai_citizen_id = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=255)
    telephone = models.CharField(max_length=20)
    job = models.CharField(max_length=255)
    holding_medical_license_no = models.CharField(max_length=20)
    organization = models.CharField(max_length=500)
    tel_organization = models.CharField(max_length=50)
    
class Donate(models.Model):
    SHIPPING = 'Shipping'
    RECEIVED = 'Received'
    CANCEL = 'Cancel'
    DONATE_STATUS = [
        (RECEIVED,'Received'),
        (SHIPPING,'Shipping'),
        (CANCEL,'Cancel')
    ]

    donator = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=DONATE_STATUS, default=SHIPPING)
    note = models.TextField()

class Receive(models.Model):
    WAIT_FOR_VERIFY = 'Wait for verify'
    VERIFIED = 'Verified'
    PACKING = 'Packing'
    SHIPPING = 'Shipping'
    CONFIRM_RECEIVED = 'Confirm received'
    RECEIVE_STATUS = [
        (WAIT_FOR_VERIFY,'Wait for verify'),
        (VERIFIED,'Verified'),
        (PACKING,'Packing'),
        (SHIPPING,'Shipping'),
        (CONFIRM_RECEIVED,'Confirm received')
    ]

    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=RECEIVE_STATUS, default=WAIT_FOR_VERIFY)
    shipping_address = models.TextField()
    shipping_id = models.CharField(max_length=30)
    note = models.TextField()