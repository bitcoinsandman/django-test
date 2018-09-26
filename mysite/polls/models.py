from django.db import models

# Create your models here.
class Objectives(models.Model):
    objectiveName = models.CharField(max_length=200, default="objective")
    objectiveDescription = models.TextField(default='undefined')
    objectiveScore = models.PositiveSmallIntegerField(default='0')

    def __str__(self):
        return self.objectiveName

class College(models.Model):
    collegeName = models.CharField(max_length=200, default="undefined")
    collegeScore = models.PositiveSmallIntegerField(default="0")
    collegeGrade = models.CharField(max_length=2, default="F")

    def __str__(self):
        return self.collegeName