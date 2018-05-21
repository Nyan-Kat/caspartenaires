# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'Post':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contract')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'create.html', args)
