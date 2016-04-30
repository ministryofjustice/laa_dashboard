from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^', views.get_password, name='password'),
    #url(r'^test_view/$', views.test_view),
    url(r'^check_all_services/$', views.check_all_services),
    # url(r'^check_service/$', views.check_service),
    url(r'^', views.view_status),


]
