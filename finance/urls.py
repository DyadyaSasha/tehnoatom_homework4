from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.base_page, name='base_page'),
    url(r'^form/$', views.form, name='form'),
    url(r'^generator/$', views.generator_view, name='generator'),
]