from django.urls import path
from .api_views import Users_list, Payments_list, Pricings_list, Requests_list, HelpCenter_list
app_name = 'UsersUrls'

urlpatterns = [
    path('users/', Users_list.as_view(), name="users_list"),
    path('payments/', Payments_list.as_view(), name="payments_list"),
    path('pricings/', Pricings_list.as_view(), name="pricings_list"),
    path('requests/', Requests_list.as_view(), name="requests_list"),
    path('complaints/', HelpCenter_list.as_view(), name="helpcenters_list"),


]
