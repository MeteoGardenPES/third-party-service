from django.core.validators import MinValueValidator
from django.db import models

class Station(models.Model):
    stationCode = models.CharField(max_length=4, primary_key=True)  # RT.1
    station = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    solarIrradiance = models.PositiveBigIntegerField()
    temperature = models.FloatField()
    precipitation = models.FloatField(validators=[MinValueValidator(0.0)])
    updateDate = models.DateTimeField(auto_now=True)


class WeatherReading(models.Model):
    station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="weather_readings",
    )
    timestamp = models.DateTimeField()
    temperature = models.FloatField(null=True, blank=True)  # ºC       (var 32)
    precipitation = models.FloatField(null=True, blank=True)  # mm       (var 35)
    solarIrradiance = models.FloatField(null=True, blank=True)  # W/m²     (var 36)

    class Meta:
        unique_together = ("station", "timestamp")
        indexes = [
            models.Index(fields=["station", "timestamp"]),
        ]
        ordering = ["timestamp"]

    def __str__(self):
        return f"{self.station.stationCode} @ {self.timestamp}"


