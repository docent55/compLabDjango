from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from .models import Work, Initiator, Rank, Position, Subdivision, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    '''Сотрудники'''

    #user = serializers.SlugRelatedField(slug_field='', read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'user', 'name')

class SubdivisionSerializer(serializers.ModelSerializer):
    '''Подразделения'''

    class Meta:
        model = Subdivision
        fields = ('id', 'name')


class PositionSerializer(serializers.ModelSerializer):
    """Должности"""

    class Meta:
        model = Position
        fields = ('id', 'name')

class RankSerializer(serializers.ModelSerializer):
    """Звания"""

    class Meta:
        model = Rank
        fields = ('id', 'name')

class InitiatorSerializer(serializers.ModelSerializer):
    """Инициаторы"""

    # rank = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # position = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # subdivision = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Initiator
        fields = ('__all__')


class WorkListSerializer(serializers.ModelSerializer):
    """Список работы"""
    subdivision = serializers.SlugRelatedField(slug_field='name', read_only=True)
    initiator = serializers.SlugRelatedField(slug_field='family_name', read_only=True)
    type_work = serializers.SlugRelatedField(slug_field='type_work', read_only=True)

    class Meta:
        model = Work
        fields = ('id', 'number', 'serial_number', 'receipt_date', 'subdivision', 'completion_date', 'initiator', 'type_work') # fields = '__all__' вывести все



class WorkAddSerializer(serializers.ModelSerializer):
    """Добавить материал"""



    class Meta:
        model = Work
        fields = ('__all__')


class WorkDetailSerializer(serializers.ModelSerializer):
    """Информация о работе"""

    initiator = serializers.SlugRelatedField(slug_field='family_name', read_only=True) # что бы отображались имена вместо ID. если отношение многие ко многим то не забыть добавить many=True
    employee = serializers.SlugRelatedField(slug_field='name', read_only=True)
    subdivision = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Work
        fields = '__all__'


class TypeWorkSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Work
        fields = ('id', 'type_work', 'slug')
