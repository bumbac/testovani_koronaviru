"""
View controller for logout function
"""
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views import View

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect("/")
