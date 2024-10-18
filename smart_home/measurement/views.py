from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorCreateUpdateSerializer, MeasurementCreateSerializer


class SensorListCreateAPIView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorRetrieveUpdateAPIView(APIView):
    def get(self, request, pk):
        try:
            sensor = Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            return Response({'error': 'Sensor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            sensor = Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            return Response({'error': 'Sensor not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SensorCreateUpdateSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        try:
            sensor = Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            return Response({'error': 'Sensor not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SensorCreateUpdateSerializer(sensor, data=request.data, partial=True)  # partial=True для поддержки частичных обновлений
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeasurementCreateAPIView(APIView):
    def post(self, request):
        serializer = MeasurementCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
