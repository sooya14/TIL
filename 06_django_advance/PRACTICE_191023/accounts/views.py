from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from django.contrib.auth.decorators import login_required  # 

from django.contrib.auth import login as auth_login, logout as auth_logout  # 

from django.contrib.auth import get_user_model  # 


@require_POST
def signup(request):
    pass


def login(request):
    pass


@login_required
def logout(request):
    pass 



