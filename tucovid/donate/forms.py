from django.forms import ModelForm
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'thai_citizen_id', 'date_of_birth', 'email', 'telephone', 'job', 'holding_medical_license_no', 'organization', 'tel_organization']

class DonateForm(ModelForm):
    class Meta:
        model = Donate
        fields = ['donator', 'item', 'quantity', 'note', 'shipping_id']

class ReceiveForm(ModelForm):
    class Meta:
        model = Receive
        fields = ['receiver', 'item', 'quantity', 'shipping_address', 'note']