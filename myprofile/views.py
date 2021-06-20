from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from .models import ProfileCustomer
from .serializers import ProfileCustomerSerializer


class ProfileCustomerListView(ListAPIView):
    queryset = ProfileCustomer.objects.all()
    serializer_class = ProfileCustomerSerializer


class ProfileCustomerDetailView(RetrieveAPIView):
    queryset = ProfileCustomer.objects.all()
    serializer_class = ProfileCustomerSerializer


class ProfileCustomerUpdateView(UpdateAPIView):
    queryset = ProfileCustomer.objects.all()
    serializer_class = ProfileCustomerSerializer
