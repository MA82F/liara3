from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import History
from rest_framework import status
from .serializers import HistorySerializer
from rest_framework.views import APIView

class HistoryView(APIView):
    def get(self, request):
        history = History.objects.all()
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

