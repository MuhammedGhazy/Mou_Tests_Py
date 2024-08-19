from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Product
from . serializers import ProductSerializers
from django.shortcuts import get_object_or_404
from . filters import ProdcutsFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.
@api_view(['GET'])
def get_all_product(request):
    #products = Product.objects.all()
    #serializers = ProductSerializers(products, many=True)
   # print(products)
    filterSet = ProdcutsFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    counter = filterSet.qs.count()
    respage = 2
    paginator = PageNumberPagination()
    paginator.page_size = respage
    queryset = paginator.paginate_queryset (filterSet.qs, request)
    serializers = ProductSerializers(queryset, many = True)
    return Response ({"products": serializers.data, 'per page': respage, 'counter':counter})

@api_view(['GET'])
def get_by_id(request,pk):
    product = get_object_or_404(Product, id = pk)
    serializer = ProductSerializers(product, many=False)
    return Response ({"product": serializer.data})

