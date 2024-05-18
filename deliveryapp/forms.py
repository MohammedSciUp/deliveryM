from django import forms
from .models import Order, Deliverer

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'order_number', 'from_location', 'to_location', 'pick_up_location',
            'pick_up_pic', 'pick_up_phone_number', 'pick_up_time', 'package_type',
            'pick_up_comment', 'delivery_location', 'delivery_pic',
            'delivery_phone_number', 'delivery_time', 'delivery_comment', 'deliverer'
        ]
        widgets = {
            'pick_up_comment': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'delivery_comment': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class DelivererForm(forms.ModelForm):
    class Meta:
        model = Deliverer
        fields = ['name', 'phone_number']

class AssignDelivererForm(forms.ModelForm):
    deliverer = forms.ModelChoiceField(queryset=Deliverer.objects.all(), required=True, label="Select Deliverer")

    class Meta:
        model = Order
        fields = ['deliverer']
