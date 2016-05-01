from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^check_all_services/', views.check_all_services),
    url(r'^edit_status/', views.edit_status),
    url(r'^update_status/', views.update_status),
    url(r'^', views.view_status),

]
