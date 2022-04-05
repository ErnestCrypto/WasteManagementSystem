from django.urls import path
from Users.views import Myview
app_name = 'UsersUrls'

urlpatterns = [
    path('', Myview.as_view(), name="myview_users"),
]
