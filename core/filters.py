from django_filters.rest_framework import FilterSet
from api.models import Students

class ProductFilter(FilterSet):
    class Meta:
        model = Students
        fields = {
            'student__first_name':['exact'],
            'student__last_name': ['exact'],
            'group__name': ['exact']
        }