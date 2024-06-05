from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
STATUS=(('PENDING','pending'),('IN_TRANSIT','in_transit'),('DELIVERED','delivered'),)
SIZES=(('SMALL','small'),('LARGE','large'),('MEDIUM','medium'),('EXTRA_LARGE','extra_large'),)
class Orders(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    size=models.CharField(max_length=50,choices=SIZES,default=SIZES[0][0])
    status=models.CharField(max_length=30,choices=STATUS,default=STATUS[0][0])
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'order by {self.customer} for {self.size}'