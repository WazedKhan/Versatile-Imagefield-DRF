from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import ProductSerializer

from .models import Product


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    queryset = Product.objects.all()
