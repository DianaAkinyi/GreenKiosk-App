from django.shortcuts import render
from rest_framework.views import APIView
from customer.models import Customer
from order.models import Order,Cart
from inventory.models import Product
from .serializers import CustomerSerializer,OrderSerializer,ProductSerializer,CartSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CustomerListView(APIView):
    def get(self,request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many = True)

        return Response(serializer.data)
    def post(self,request):
        serializer =CustomerSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status =status.HTTP_400_CREATED)

class CustomerDetailView(APIView):
    def get(self,request,id,format=None):
        customer =Customer.objects.get(id=id)
        serializer= CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        customer =Customer.objects.get(id=id)
        serializer= CustomerSerializer(customer,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_200_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_CREATED)

    def delete(self,request,id,format=None):
        customer= Customer.objects.get(id=id)
        customer.delete()
        return Response("customer_deleted", status=HTTP_204_CREATED)


class OrderListView(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            order = Order.objects.get(id=id)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response("Order not found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        try:
            order = Order.objects.get(id=id)
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response("Order not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, format=None):
        try:
            order = Order.objects.get(id=id)
            order.delete()
            return Response("Order deleted", status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response("Order not found", status=status.HTTP_404_NOT_FOUND)

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response("Product not found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response("Product not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, format=None):
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response("Product deleted", status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response("Product not found", status=status.HTTP_404_NOT_FOUND)

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            cart = Cart.objects.get(id=id)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response("Cart not found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        try:
            cart = Cart.objects.get(id=id)
            product_id = request.data.get('product_id')
            try:
                product = Product.objects.get(id=product_id)
                cart.products.add(product)
                cart.save()
                serializer = CartSerializer(cart)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response("Product not found", status=status.HTTP_404_NOT_FOUND)
        except Cart.DoesNotExist:
            return Response("Cart not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, format=None):
        try:
            cart = Cart.objects.get(id=id)
            cart.delete()
            return Response("Cart deleted", status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response("Cart not found", status=status.HTTP_404_NOT_FOUND)


