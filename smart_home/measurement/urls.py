from django.urls import path
from .views import SensorListCreateAPIView, SensorRetrieveUpdateAPIView, MeasurementCreateAPIView

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view(), name='sensor-detail-update'),
    path('measurements/', MeasurementCreateAPIView.as_view(), name='measurement-create'),
]
