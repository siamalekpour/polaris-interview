from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class TripView(TemplateView):
    template_name = "trip_list.html"
