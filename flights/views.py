from rest_framework.generics import ListAPIView, RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer,DetailSeralizer,UpdateSeralizer


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer

class BookingDetails(RetrieveAPIView):
	queryset= Booking.objects.all()
	serializer_class = DetailSeralizer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'

class BookingUpdate(RetrieveUpdateAPIView):
	queryset= Booking.objects.all()
	serializer_class = UpdateSeralizer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'

class BookingDelete(DestroyAPIView):
	queryset= Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'




