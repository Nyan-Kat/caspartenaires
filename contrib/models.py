from re import compile

from django.urls import resolve, Resolver404
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from django.conf import settings
from django.shortcuts import redirect

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        if not request.user.is_authenticated:
            path = request.path_info
            if path not in settings.LOGIN_EXEMPT_URLS:
                denied = True
                for pattern in settings.LOGIN_EXEMPT_URL_PATTERNS:
                    if pattern.match(path) is not None:
                        denied = False
                        break
                if denied is True:
                    return redirect(settings.LOGIN_URL)
                    # try:
                    #     match = resolve(request.path_info)
                    #     request.session['after_login'] = request.path_info
                    # except Resolver404:
                    #     try:
                    #         del request.session['after_login']
                    #     except KeyError:
                    #         pass
                    # return HttpResponseRedirect(settings.LOGIN_URL)
