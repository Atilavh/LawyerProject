from django import forms


class UserRegisterForm(forms.Form):
    full_name = forms.CharField(
        error_messages={'required': 'Please enter your full name.'},
        max_length=100,
        widget=forms.TextInput(attrs={
            'id': 'movakel__name-family',
            'class': 'vakil-form__input',
            'placeholder': 'نام و نام خانوادگی',
        })
    )
    phone_number = forms.CharField(
        error_messages={'required': 'Please enter your phone number.'},
        max_length=11,
        widget=forms.TextInput(attrs={
            'id': 'movakel__phone',
            'class': 'vakil-form__input',
            'placeholder': 'شماره تماس'
        })
    )
