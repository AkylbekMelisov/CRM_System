from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)
    Order_count = models.PositiveIntegerField(default=0)
    
