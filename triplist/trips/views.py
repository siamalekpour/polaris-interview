from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from models import *
from serializers import *

# Create your views here.
class TripListView(TemplateView):
    template_name = "trip_list.html"

    def get_context_data(self, **kwargs):
        context = super(TripListView, self).get_context_data(**kwargs)
        context['trips'] = Trip.objects.all()
        return context


class TripDetailView(TemplateView):
    template_name = "trip_detail.html"

    def get_context_data(self, **kwargs):
        context = super(TripDetailView, self).get_context_data(**kwargs)
        try:
            trip = Trip.objects.select_related('type', 'country__continent',).get(id=context['pk'])
        except Trip.DoesNotExist:
            return HttpResponseNotFound()
        else:
            context['trip'] = trip
            context['travelers'] = trip.traveler_set.all()
            context['destinations'] = trip.destination_set.all()
            return context


class TripApiList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class TripApiDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# class TripApiList(APIView):
# 
#     def get(self, request, format=None):
#         trips = Trip.objects.all()
#         serializer = TripSerializer(trips, many=True, context={'request': request})
#         return Response(serializer.data)
# 
# 
# class TripApiDetail(APIView):
#     def get(self, request, id, format=None):
#         trip = None
#         try:
#             trip = Trip.objects.get(id=id)
#         except Trip.DoesNotExist:
#             raise Http404
#         serializer = TripSerializer(trip)
#         return Response(serializer.data)