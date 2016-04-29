from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^', views.get_password, name='password'),
    #url(r'^test_view/$', views.test_view),
    url(r'^ajax/$', views.ajax),
    url(r'^', views.main_page),


]
