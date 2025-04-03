from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} ({self.address})"


class Participant(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


# Create your models here.
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    organizer_email = models.EmailField(blank=False)
    organizer_name = models.CharField(blank=True, max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    Participants = models.ManyToManyField(Participant, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.slug}"
