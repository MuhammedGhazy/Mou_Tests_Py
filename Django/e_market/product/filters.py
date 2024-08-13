from .models import Product
import django_filters

class ProdcutsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")
    keyword = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    minprice = django_filters.NumberFilter(field_name='price' or 0, lookup_expr='gte')
    maxprice = django_filters.CharFilter(field_name='price' or 1000000, lookup_expr='lte')
    class Meta():
        model = Product
        fields = ('category', 'brand','keyword', 'minprice', 'maxprice')