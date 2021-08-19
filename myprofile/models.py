from django.db import models

class New(models.Model):
	name = models.TextField()
	email= models.EmailField()
	comment = models.TextField()

def __str__(self):
	return self.name