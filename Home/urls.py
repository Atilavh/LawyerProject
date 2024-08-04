from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('LoginPage', views.login_page, name='login_page'),
    # <--This urls for django_render_partial
    # path('site-header', views.header_render_partial, 'header_render_partial'),
    # path('site-footer', views.footer_render_partial, 'footer_render_partial')
    # -->
]
