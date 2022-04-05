# Creating our views
from django.views import View
from django.http import HttpResponse


class Myview(View):
    greeting = "Hello this is users"

    def get(self, request):
        return HttpResponse(self.greeting)
