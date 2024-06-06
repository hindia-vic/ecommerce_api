from django.urls import path
from .views import OrderCreation,OrderDetail,OrderStatus,UserOrders,userOrderDetail

urlpatterns=[
    path('',OrderCreation.as_view(),name='order'),
    path('<int:order_id>/',OrderDetail.as_view(),name='detail'),
    path('update/<int:order_id>/',OrderStatus.as_view(),name='updatestatus'),
    path('user/<int:user_id>/',UserOrders.as_view(),name='user_orders'),
    path('user/<int:user_id>/<int:order_id>/',userOrderDetail.as_view(),name='user_order_detail')
]