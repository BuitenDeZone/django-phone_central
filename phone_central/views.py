"""Django views."""

from django.shortcuts import render
from django.contrib import messages


def index(request):
    """Render the index page."""
    messages.info(request, 'Random info message')
    return render(request, 'index.html')
