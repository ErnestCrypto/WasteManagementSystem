from django.urls import path
from Users import api_views
app_name = 'UsersUrls'

urlpatterns = [
    path('auth/', api_views.Auth.as_view(), name="auth"),
    path('auth_details/', api_views.Auth_details.as_view(), name="auth_details"),
    path('users/', api_views.User_list.as_view(), name="login_list"),
    path('users/<int:pk>/',
         api_views.User_details.as_view(), name="login_details"),
    path('payments/', api_views.Payments_list.as_view(), name="payments_list"),
    path('payments/<int:pk>/', api_views.Payments_details.as_view(),
         name="payments_details"),
    path('pricings/', api_views.Pricings_list.as_view(), name="pricings_list"),
    path('pricings/<int:pk>', api_views.Pricings_details.as_view(),
         name="pricings_details"),
    path('requests/', api_views.Requests_list.as_view(), name="requests_list"),
    path('requests/<int:pk>/', api_views.Requests_details.as_view(),
         name="requests_details"),
    path('complaints/', api_views.HelpCenter_list.as_view(),
         name="helpcenters_list"),
    path('complaints/<int:pk>/', api_views.HelpCenter_details.as_view(),
         name="helpcenters_details"),


]
