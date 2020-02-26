from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    
    # List comprehensions to create lists of months and years for use with credit card details
    MONTHS = [(i, i) for i in range(1, 12)]
    YEARS = [(i, i) for i in range(2020, 2030)]

    card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (back of card)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTHS, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEARS, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)