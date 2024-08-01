from django.shortcuts import render


# Create your views here.

def header_render_partial(request):
    return render(request, 'Header/HeaderRenderPartial.html', {})


def home_page(request):
    return render(request, 'layout/Base.html')


def index_page(request):
    return render(request, 'Shared/index.html')


def footer_render_partial(request):
    return render(request, 'Footer/FooterRenderPartial.html', {})
