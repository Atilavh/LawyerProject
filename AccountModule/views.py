from django.shortcuts import render
from AccountModule.models import User

from AccountModule.forms import UserRegisterForm


# Create your views here.

def LoginPage(request):
    return render(request, 'Accounts/LoginPage.html')


def UserRegister(request):
    user_register = UserRegisterForm(request.POST)
    if user_register.is_valid():
        FullName = user_register.cleaned_data.get('full_name')
        PhoneNumber = user_register.cleaned_data.get('phone_number')
        user: bool = User.objects.filter(PhoneNumber__iexact=PhoneNumber).exists()
        if user:
            user_register.add_error('phone_number', 'شما قبلا ثبت نام کردید!')
        else:
            new_user = User(
                FullName=FullName,
                PhoneNumber=PhoneNumber,
            )
            new_user.save()
    context = {
        'User': user_register
    }
    return render(request, 'Accounts/LoginPage.html', context)
