from django.db import models

# Create your models here.
class Feedback(models.Model):
    feedback_content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
   
    ratings=models.CharField(max_length=5)
    feedback_status=models.CharField(max_length=20)
