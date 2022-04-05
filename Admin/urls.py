from django.urls import path
from Admin.views import Myview
from rest_framework.urlpatterns import format_suffix_patterns
from Admin import api_views
app_name = 'AdminUrls'

urlpatterns = [
    path('/admins/', api_views.Adminstrators_details.as_view(),
         name="administrators_details"),
    path('/drivers/', api_views.Drivers_details.as_view(),
         name="drivers_details"),
    path('/trucks/', api_views.Trucks_details.as_view(),
         name="trucks_details"),
    path('/pricings/', api_views.Pricings_details.as_view(),
         name="pricings_details"),
    path('/requests/', api_views.Requests_details.as_view(),
         name="requests_details"),
    path('/complaints/', api_views.HelpCenter_details.as_view(),
         name="helpcenter_details"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
