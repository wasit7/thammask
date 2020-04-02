from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=500)
    address = models.TextField()

    def __str__(self):
        return str(self.hospital_name)

class DonateItem(models.Model):
    donate_item_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit = models.CharField(max_length=50)
    show_item = models.BooleanField(default=True)

    def __str__(self):
        return str(self.donate_item_name)

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.item_name

class Job(models.Model):
    job_name = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.job_name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telephone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

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

    donator = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(DonateItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=100, choices=DONATE_STATUS, default=SHIPPING)
    shipping_id = models.CharField(max_length=30, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

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
    
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    holding_medical_license_no = models.CharField(max_length=20, null=True, blank=True)
    shipping_id = models.CharField(max_length=30)
    note = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=RECEIVE_STATUS, default=WAIT_FOR_VERIFY)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.receiver)

class Review(models.Model):
    receive = models.OneToOneField(Receive, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.receive)