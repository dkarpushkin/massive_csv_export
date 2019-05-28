from django.urls import path
from .views import CustomersViewSet

urlpatterns = [
    path('csv/', CustomersViewSet.as_view(actions={'get': 'csv_list'})),
]
