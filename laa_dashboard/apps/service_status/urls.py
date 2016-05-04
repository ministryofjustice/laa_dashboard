from django.conf.urls import url
from django.views.generic import RedirectView


from . import views

urlpatterns = [
    url(r'^get_statuses/', views.GetStatuses.as_view()),
    url(r'^edit_status/', views.EditStatus.as_view()),
    url(r'^view_status/', views.ViewStatus.as_view()),
    url(r'^update_status/', views.UpdateStatus.as_view()),
    url(r'^simple_table/', views.SimpleTable.as_view()),
    url(r'^view_services/', views.ViewServices.as_view()),
    url(r'^', RedirectView.as_view(url='view_services/'))

]
