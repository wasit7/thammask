from django.forms import ModelForm
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'full_name', 'address', 'email', 'telephone', 'job', 'holding_medical_license_no', 'organization']

class DonateForm(ModelForm):
    class Meta:
        model = Donate
        fields = ['created_by', 'donator', 'item', 'quantity', 'note', 'shipping_id']

class ReceiveForm(ModelForm):
    class Meta:
        model = Receive
        fields = ['created_by', 'receiver', 'item', 'quantity', 'shipping_address', 'note']