from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions



from django_filters.rest_framework import DjangoFilterBackend

from .models import Work, TypeWork, Initiator, Rank, Position, Subdivision, Employee

from .serializers import WorkListSerializer, WorkDetailSerializer, TypeWorkSerializer, \
    WorkAddSerializer, InitiatorSerializer, RankSerializer, PositionSerializer, SubdivisionSerializer, EmployeeSerializer

from .service import WorkFilter

class WorkListAPIView(ListAPIView):

    serializer_class = WorkListSerializer
    queryset = Work.objects.all()
    lookup_field = 'id'
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WorkFilter
    # permission_classes = [permissions.IsAuthenticated]

class WorkAddAPIView(CreateAPIView):
    '''Добовление работы'''
    queryset = Work.objects.all()
    serializer_class = WorkAddSerializer

class WorkDetailView(RetrieveUpdateDestroyAPIView):
    """Вывод информации о материале"""
    queryset = Work.objects.all()
    serializer_class = WorkDetailSerializer

class TypeWorkListAPIView(ListAPIView):

    serializer_class = TypeWorkSerializer
    queryset = TypeWork.objects.all()

class InitiatorListAPIView(ListCreateAPIView):
    """Вывод и добавление инифиаторов"""

    queryset = Initiator.objects.all()
    serializer_class = InitiatorSerializer

class RankListAPIView(ListCreateAPIView):
    """Вывод и добавление имени званий"""

    queryset = Rank.objects.all()
    serializer_class = RankSerializer

class RankUpadateDeleteView(RetrieveUpdateDestroyAPIView):

    queryset = Rank.objects.all()
    serializer_class = RankSerializer

class PositionListAPIView(ListCreateAPIView):
    """Вывод и добавление имени должности"""

    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """Обновление и удаление должностей"""

    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class SubdivisionListAPIView(ListCreateAPIView):
    '''Вывод и добавление подразделений'''

    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer

class SubdivisionUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    '''Обновление и удаление подразделений'''

    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer

class EmployeeListView(ListAPIView):
    '''Вывод списка сотрудников'''

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer