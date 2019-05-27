from django.urls import path
from .views import CustomersListView

urlpatterns = [
    path('csv/', CustomersListView.as_view()),
]