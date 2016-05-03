from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^check_all_services/', views.check_all_services),
    url(r'^edit_status/', views.EditStatus.as_view()),
    url(r'^view_status/', views.ViewStatus.as_view()),
    url(r'^update_status/', views.UpdateStatus.as_view()),
    url(r'^simple_table/', views.SimpleTable.as_view()),
    url(r'^', views.ViewServices.as_view()),

]
