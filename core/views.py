from rest_framework import viewsets
from .models import User, Record
from .serializers import UserSerializer, RecordSerializer
from .permissions import IsAdmin, IsViewer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum


# USER APIs
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer
from .permissions import IsAdmin, IsViewer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdmin()]   # only admin
        return [IsViewer()]      # others can view


# RECORD APIs
from rest_framework.permissions import IsAuthenticated

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated(), IsViewer()]

# DASHBOARD API
@api_view(['GET'])
def dashboard_summary(request):
    income = Record.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = Record.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    return Response({
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    })



from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import Record

@api_view(['GET'])
def dashboard_summary(request):
    income = Record.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = Record.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    return Response({
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    })

from django.shortcuts import render

# Create your views here.
