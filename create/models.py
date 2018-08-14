from django.db import models

from django.utils import timezone


class TourInfo(models.Model):
    tour_id = models.AutoField(primary_key=True)
    #user_id = models.CharField(max_length=20)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    geo_hash = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    like = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.BigIntegerField()
    money = models.BigIntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class SpotInfo(models.Model):
    tour_id = models.BigIntegerField()
    spot_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
