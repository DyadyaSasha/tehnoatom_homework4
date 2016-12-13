from django import forms
from datetime import date

class ChargeForm(forms.Form):
    transaction = forms.DecimalField(label="Transaction")
    dat = forms.DateField(label="Date")
    
    def clean(self):
        cleaned_data = super(ChargeForm, self).clean()
        transaction = cleaned_data.get('transaction')
        dat = cleaned_data.get('dat')
        if transaction == 0:
            self.add_error('transaction', "Transaction can't equal zero")
        if transaction < 0 and dat > date.today():
            self.add_error('transaction', "Invalid transaction")
        return cleaned_data