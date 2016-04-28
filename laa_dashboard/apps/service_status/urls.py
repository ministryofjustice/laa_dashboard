from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^', views.get_password, name='password'),
    url(r'^', views.main_page, name='password'),
]
