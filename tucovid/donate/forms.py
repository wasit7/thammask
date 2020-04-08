from django.forms import ModelForm
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'full_name', 'email', 'telephone']

class DonateForm(ModelForm):
    class Meta:
        model = Donate
        fields = ['donator', 'item', 'quantity', 'note', 'shipping_id']

class ReceiveForm(ModelForm):
    class Meta:
        model = Receive
        fields = ['receiver', 'item', 'hospital', 'job', 'holding_medical_license_no', 'note']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer', 'receive', 'score', 'comment']