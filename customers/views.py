import csv

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


class CustomersListView(ListAPIView):
    
    queryset = Customer.objects.all().prefetch_related('phones', 'emails')
    filename = 'customers.csv'

    def get_renderer_context(self):

        context = super().get_renderer_context()
        context.update({
            'header': ['id', 'first_name', 'last_name', 'phones__number', 'emails__address'],
            'labels': {
                'id': 'customer.id',
                'first_name': 'customer.first_name',
                'last_name': 'customer.last_name',
                'emails__address': 'phone.number',
                'phones__number': 'email.address',
            }
        })
        return context

    def render_csv_generator(self, data):
        csv_buffer = Echo()
        csv_writer = csv.writer(csv_buffer)
        yield csv_writer.writerow(
            ['customer.id', 'customer.first_name', 'customer.last_name', 'phone.number', 'email.address']
        )
        for row in data:
            yield csv_writer.writerow(row)

    def list(self, request, *args, **kwargs):

        qs = self.queryset.values_list('id', 'first_name', 'last_name', 'phones__number', 'emails__address')

        resp = StreamingHttpResponse(self.render_csv_generator(list(qs)), content_type='text/csv')

        resp['Content-Disposition'] = f'attachment; filename="{self.filename}"'
        return resp
