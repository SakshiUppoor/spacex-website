from django.db import models

# Create your models here.

class Launches(models.Model):

    flight_number = models.IntegerField(default=0)
    launch_date = models.DateField(null=True, blank=True)
    rocket_name = models.CharField(max_length=50,  blank=True, null=True)
    mission_patch_link = models.CharField( max_length=200,  blank=True, null=True)
    reddit_launch = models.CharField( max_length=200,  blank=True, null=True)
    video_link = models.CharField( max_length=200,  blank=True, null=True)
    wikipedia = models.CharField( max_length=200,  blank=True, null=True)
    article_link = models.CharField( max_length=200,  blank=True, null=True)
    details = models.CharField( max_length=1000,  blank=True, null=True)
    launch_success = models.CharField( max_length=10,  blank=True, null=True)

    def __str__(self):
        return str(self.flight_number)
    
class Mission(models.Model):
    mission_name = models.CharField(max_length=10)
    mission_id = models.CharField(max_length=10)
    twitter = models.CharField( max_length=200,  blank=True, null=True)
    wikipedia = models.CharField( max_length=200,  blank=True, null=True)
    website = models.CharField( max_length=200,  blank=True, null=True)
    description = models.CharField( max_length=1000,  blank=True, null=True)

    def __str__(self):
        return self.mission_id

class Core(models.Model):

    core_serial = models.CharField(max_length=25)
    launch_date = models.DateField(blank=True, null=True)
    mission_name = models.CharField(max_length=25)
    mission_flight = models.IntegerField(default=0)
    details = models.CharField( max_length=1000,  blank=True, null=True)


    def __str__(self):
        return self.core_serial

class Rocket(models.Model):

    rocket_number = models.IntegerField(default=0)
    active = models.CharField( max_length=10,  blank=True, null=True)
    cost_per_launch = models.IntegerField(default=0)
    country = models.CharField( max_length=200,  blank=True, null=True)
    rocket_name = models.CharField( max_length=200,  blank=True, null=True)
    rocket_id = models.CharField(max_length=10)
    first_flight = models.DateField(blank=True, null=True)
    description = models.CharField( max_length=1000,  blank=True, null=True)
    wikipedia = models.CharField( max_length=200,  blank=True, null=True)

    def __str__(self):
        return self.rocket_name
    