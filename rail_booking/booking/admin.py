
from django.contrib import admin
from .models import Train, Booking

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('train_number', 'train_name', 'from_station', 'to_station','date', 'departure_time', 'available_seats', 'fare')
    list_filter = ('from_station', 'to_station', 'date')
    search_fields = ('train_number', 'train_name', 'from_station', 'to_station')
    ordering = ('train_number',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'train', 'date_of_journey', 'seats_booked', 'status', 'booking_time')
    list_filter = ('status', 'date_of_journey')
    search_fields = ('user__username', 'train__train_number', 'train__train_name')
    ordering = ('-booking_time',)
