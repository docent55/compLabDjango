from django_filters import rest_framework as filters
from .models import Work

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class WorkFilter(filters.FilterSet):
    type_work = CharFilterInFilter(field_name='type_work__type_work', lookup_expr='in')
    # receipt_date = filter.RangeFilter()

    class Meta:
        model = Work
        fields = ['type_work', 'receipt_date']