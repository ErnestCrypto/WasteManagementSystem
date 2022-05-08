from django.urls import path
from Users import api_views
from rest_framework.authtoken import views

app_name = 'UsersUrls'

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('example/', api_views.ExampleView.as_view(), name="clientlist"),
    path('client/', api_views.UserList.as_view(), name="clientlist"),
    path('client/<int:pk>/', api_views.UserDetail.as_view(), name="clientdetail"),
    path('test/', api_views.Test.as_view(), name="test"),
    path('auth/', api_views.Auth.as_view(), name="auth"),
    path('auth_details/', api_views.Auth_details.as_view(), name="auth_details"),
    path('users/', api_views.User_list.as_view(), name="user_list"),
    path('users/<int:pk>/',
         api_views.User_details.as_view(), name="user_details"),
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
