from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class ToDoList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()
	date_added = models.CharField(max_length=300, default=str(datetime.today()).split()[0])
	priority = models.IntegerField(default=0)

	def __str__(self):
		return self.text