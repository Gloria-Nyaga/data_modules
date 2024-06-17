from django.db import models

class Course(models.Model):
    course_title = models.CharField(max_length = 20)
    course_description = models.TextField ()
    course_start_date = models.DateField ()
    course_end_date = models.DateField ()
    course_code = models.PositiveSmallIntegerField ()
    course_grading_system = models.TextField ()
    course_materials = models.TextField ()
    course_fee = models.PositiveSmallIntegerField ()
    course_unit = models.TextField ()
    course_outline = models.TextField ()
    course_fee = models.PositiveSmallIntegerField ()

# Create your models here.
