from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.item_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    thai_citizen_id = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=255)
    telephone = models.CharField(max_length=20)
    job = models.CharField(max_length=255)
    holding_medical_license_no = models.CharField(max_length=20, null=True, blank=True)
    organization = models.CharField(max_length=500, null=True, blank=True)
    tel_organization = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.full_name
    
class Donate(models.Model):
    SHIPPING = 'Shipping'
    RECEIVED = 'Received'
    CANCEL = 'Cancel'
    DONATE_STATUS = [
        (RECEIVED,'Received'),
        (SHIPPING,'Shipping'),
        (CANCEL,'Cancel')
    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    donator = models.CharField(max_length=255, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=100, choices=DONATE_STATUS, default=SHIPPING)
    shipping_id = models.CharField(max_length=30, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.donator)

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
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.CharField(max_length=255, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=100, choices=RECEIVE_STATUS, default=WAIT_FOR_VERIFY)
    shipping_address = models.TextField(null=True, blank=True)
    shipping_id = models.CharField(max_length=30)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.receiver)

class Review(models.Model):
    receive = models.OneToOneField(Receive, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return str(self.receive)