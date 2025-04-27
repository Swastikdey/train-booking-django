from django import forms
from .models import Booking

class SearchTrainForm(forms.Form):
    from_station = forms.CharField(max_length=100, label='From')
    to_station = forms.CharField(max_length=100, label='To')
    date = forms.DateField(widget=forms.SelectDateWidget, label='Journey Date')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seats_booked']
        widgets = {
            'seats_booked': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }
