from django.db import models

class candidates(models.Model):
    EMPLOYEEMENT_CHOICES=[
        ('S','Student'),
        ('P','Working Professional'),
        ('NA','Not Applicable'),
    ]

    first_name = models.CharField(max_length=20)
    last_name =  models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField()
    street_address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    employement_status = models.CharField(
        max_length = 15,
        choices = EMPLOYEEMENT_CHOICES
    )
    year_of_passing = models.IntegerField()
    skills = models.TextField()
    resume = models.FileField(upload_to='uploads/')


    def __str__(self):
        return self.first_name