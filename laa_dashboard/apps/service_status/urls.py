from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^check_all_services/', views.check_all_services),
    url(r'^edit_status/', views.edit_status),
    url(r'^view_status/', views.view_status),
    url(r'^update_status/', views.UpdateStatus.as_view()),
    url(r'^simple_table/', views.SimpleTable.as_view()),
    url(r'^', views.ViewServices.as_view()),

]
