import csv

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework_csv.renderers import CSVStreamingRenderer
from django.http import StreamingHttpResponse
from .models import Customer


class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


class CustomersViewSet(viewsets.ModelViewSet):
    
    queryset = Customer.objects.all().prefetch_related('phones', 'emails')
    filename = 'customers.csv'

    def render_csv_generator(self, queryset, pagesize=2000000):
        """
        Generator for StreamingHttpResponse
        """
        csv_buffer = Echo()
        csv_writer = csv.writer(csv_buffer)
        yield csv_writer.writerow(
            ['customer.id', 'customer.first_name', 'customer.last_name', 'phone.number', 'email.address']
        )
        offset = 0
        data = list(queryset[offset: offset + pagesize])

        while data:
            for row in data:
                yield csv_writer.writerow(row)
            offset += pagesize
            data = list(queryset[offset: offset + pagesize])

    def csv_list(self, request, *args, **kwargs):
        """
        Customers list in CSV

        """
        qs = self.queryset.values_list('id', 'first_name', 'last_name', 'phones__number', 'emails__address')

        resp = StreamingHttpResponse(self.render_csv_generator(qs), content_type='text/csv')

        resp['Content-Disposition'] = f'attachment; filename="{self.filename}"'
        return resp
