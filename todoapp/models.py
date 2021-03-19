from typing import Text
from django.db import models

# Create your models here.

class Todo(models.Model):
    Edit_id=models.AutoField(primary_key=True)
    Text=models.TextField(max_length=10000,default='')