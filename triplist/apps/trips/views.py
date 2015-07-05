from django.http import HttpResponseNotFound
from django.views.generic import TemplateView
from rest_framework import mixins, generics

from serializers import *


# Create your views here.
class TripListView(TemplateView):
    template_name = "trip_list.html"

    def get_context_data(self, **kwargs):
        context = super(TripListView, self).get_context_data(**kwargs)
        trips = Trip.objects.all()
        return {'trips': trips}


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

            # TODO: Use/Create a responsive javascript masonry plugin.
            # TODO: For now I'm splitting media into two lists to show seporatly in two columns the template.
            media = Media.objects.filter(destination__trip=trip)
            context['temp_media_1'] = media[::2]
            context['temp_media_2'] = media[1::2]

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