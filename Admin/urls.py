from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Admin import api_views
app_name = 'AdminUrls'

urlpatterns = [
    path('auth/', api_views.Auth.as_view(),
         name="auth"),
    path('logged/', api_views.LoggedInUsers.as_view(),
         name="auth"),
    path('logout/', api_views.Logout.as_view(),
         name="auth"),
    path('create/', api_views.Create.as_view(),
         name="create"),
    path('admins/', api_views.Adminstrators_list.as_view(),
         name="administrators_list"),
    path('admins/<int:pk>', api_views.Adminstrators_details.as_view(),
         name="administrators_details"),
    path('drivers/', api_views.Drivers_list.as_view(),
         name="drivers_list"),
    path('drivers/<int:pk>', api_views.Drivers_details.as_view(),
         name="drivers_details"),
    path('trucks/', api_views.Trucks_list.as_view(),
         name="trucks_list"),
    path('trucks/<int:pk>', api_views.Trucks_details.as_view(),
         name="trucks_details"),
    path('pricings/', api_views.Pricings_list.as_view(),
         name="pricings_list"),
    path('pricings/<int:pk>', api_views.Pricings_details.as_view(),
         name="pricings_details"),
    path('requests/', api_views.Requests_list.as_view(),
         name="requests_list"),
    path('requests/<int:pk>', api_views.Requests_details.as_view(),
         name="requests_details"),
    path('complaints/', api_views.HelpCenter_list.as_view(),
         name="helpcenter_list"),
    path('complaints/<int:pk>', api_views.HelpCenter_details.as_view(),
         name="helpcenter_details"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
