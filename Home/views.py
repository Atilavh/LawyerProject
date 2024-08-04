from django.shortcuts import render


# Create your views here.


def header_partial(request):
    return render(request, 'Header/HeaderRenderPartial.html')


def index(request):
    return render(request, 'layout/Base.html')


def login_page(request):
    return render(request, 'Accounts/LoginPage.html')


def footer_partial(request):
    return render(request, 'Footer/FooterRenderPartial.html')
