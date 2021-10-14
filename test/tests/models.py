from django.db import models
class Test(models.Model):
    name = models.TextField()

class Lol(models.Model):
    tes = models.ForeignKey(Test, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
