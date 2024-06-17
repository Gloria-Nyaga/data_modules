from django.db import models

class Class(models.Model):
    class_name = models.CharField(max_length = 20)
    class_capacity = models.PositiveSmallIntegerField ()
    class_schedule = models.TextField ()
    class_attendance = models.PositiveSmallIntegerField ()
    class_projects = models.TextField ()
    class_activities = models.TextField ()
    class_representatives = models.TextField ()
    class_assignments = models.TextField ()
    class_policies = models.TextField ()
    class_requirements = models.TextField ()
    class_members_image = models.ImageField ()

# Create your models here.
