from django.shortcuts import render
from .serializers import OrderSerializer,OrderDetailSerializer,OrderStatusUpdateSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from . models import Orders


User=get_user_model()

class OrderCreation(generics.GenericAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes=[IsAuthenticated]


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(customer=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   

class OrderDetail(generics.GenericAPIView):
    serializer_class=OrderDetailSerializer
    permission_classes=[IsAuthenticated]
    def get(self,request,order_id):
        order=get_object_or_404(Orders,pk=order_id)
        serializer=self.serializer_class(instance=order)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,order_id):
        order=get_object_or_404(Orders,id=order_id)
        serializer=self.serializer_class(instance=order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(error=serializer.error,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,order_id):
        order=get_object_or_404(Orders,pk=order_id)
        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OrderStatus(generics.GenericAPIView):
    serializer_class=OrderStatusUpdateSerializer

    def put(self,request,order_id):
        order=get_object_or_404(Orders,id=order_id)
        serializer=self.serializer_class(instance=order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(error=serializer.error,status=status.HTTP_400_BAD_REQUEST)


class UserOrders(generics.GenericAPIView):
   serializer_class=OrderDetailSerializer

   def get(self,request,user_id):
        user=User.objects.get(pk=user_id)
        order=Orders.objects.all().filter(customer=user)
        serializer=self.serializer_class(instance=order,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
   
class userOrderDetail(generics.RetrieveAPIView):
    serializer_class=OrderDetailSerializer
    def get_object(self):
        user_id = self.kwargs['user_id']
        order_id = self.kwargs['order_id']
        user = get_object_or_404(User, pk=user_id)
        order = get_object_or_404(Orders, customer=user, pk=order_id)
        return order