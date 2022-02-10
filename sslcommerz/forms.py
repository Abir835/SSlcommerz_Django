from django import forms


Options = [
        ('1', 'SSLCOMMERZ'),
        ('2', 'cash on'),
    ]


class sslForm(forms.Form):
    category = forms.ChoiceField(choices=Options)

