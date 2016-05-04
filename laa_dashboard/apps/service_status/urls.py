from django.conf.urls import url
from django.views.generic import RedirectView


from . import views

urlpatterns = [

    url(r'^view_services/', views.ViewServicesList.as_view()),
    url(r'^update_services/', views.UpdateServicesList.as_view()),
    url(r'^simple_table/', views.SimpleTable.as_view()),
    url(r'^view_status/', views.ViewServiceStatus.as_view()),
    url(r'^update_status/', views.UpdateServiceStatus.as_view()),
    url(r'^get_statuses/', views.GetStatuses.as_view()),
    url(r'^', RedirectView.as_view(url='view_services/'))

]
