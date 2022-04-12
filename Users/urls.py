from django.urls import path
from .api_views import Users_list
app_name = 'UsersUrls'

urlpatterns = [
    path('users/', Users_list.as_view(), name="users_list"),
]
