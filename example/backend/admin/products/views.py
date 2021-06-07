from django.http import response
from rest_framework import viewsets, response, status
from rest_framework.views import APIView
from .models import Product, User
from .seralizers import ProductSerializer
import random


class ProductViewSet(viewsets.ViewSet):
    # /api/products
    def getAllProducts(self, req):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return response.Response(serializer.data)

    # /api/products
    def postProduct(self, req):
        serializer = ProductSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    # /api/products/<str:id>
    def getProduct(self, req, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return response.Response(serializer.data)

    # /api/products/<str:id>
    def updateProduct(self, req, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # /api/products/<str:id>
    def deleteProduct(self, req, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return response.Response(data=req.data, status=status.HTTP_202_ACCEPTED)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return response.Response({
            "id": user.id
        })
