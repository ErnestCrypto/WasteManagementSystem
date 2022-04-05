from django.urls import path
from Admin.views import Myview
app_name = 'AdminUrls'

urlpatterns = [
    path('', Myview.as_view(), name="myview_users")
]
