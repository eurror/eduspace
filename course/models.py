from django.db import models

class CourseCategory(models.Model):
    
    title = models.CharField(max_length=50)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='course_category')
