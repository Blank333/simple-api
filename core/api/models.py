from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Todo(models.Model):
    task = models.CharField(max_length = 256)
    completed = models.BooleanField(default = False, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    deadline = models.DateTimeField(default= datetime.today() + timedelta(days=1))
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.task