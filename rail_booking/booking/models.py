from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
class Train(models.Model):
    train_number = models.CharField(max_length=10, unique=True)
    train_name = models.CharField(max_length=100)
    from_station = models.CharField(max_length=100)
    to_station = models.CharField(max_length=100)
    date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    fare = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.train_number} - {self.train_name}"

class Booking(models.Model):
    STATUS_CHOICES = (
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='bookings')
    date_of_journey = models.DateField()
    booking_time = models.DateTimeField(auto_now_add=True)
    seats_booked = models.PositiveIntegerField(
    default=1,
    validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ]
)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CONFIRMED')

    def __str__(self):
        return f"Booking {self.id} - {self.user.username} - {self.train.train_name} - {self.train.train_number}"
