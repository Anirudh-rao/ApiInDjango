from django.db import models

# Create your models here.
"""
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. 
Generally, each model maps to a single database table.
"""
class Note(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_list =  models.DateTimeField(auto_now_add=True)

def __str__(self):
	return '%s %s' % (self.title, self.body)
