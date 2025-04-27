from django.shortcuts import render, redirect, get_object_or_404
from .models import Train, Booking
from .forms import SearchTrainForm, BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.

#def available_trains(request):
#    trains = Train.objects.all()
 #   return render(request, 'booking/available_trains.html', {'trains':trains})


def search_trains_view(request):
    if request.method == 'POST':
        form = SearchTrainForm(request.POST)
        if form.is_valid():
            from_station = form.cleaned_data['from_station']
            to_station = form.cleaned_data['to_station']
            journey_date = form.cleaned_data['date']

            # Redirect with parameters (GET method)
            return redirect('trains_list', from_station=from_station, to_station=to_station, journey_date=journey_date)
    else:
        form = SearchTrainForm()
    
    return render(request, 'booking/search_trains.html', {'form': form})

def trains_list_view(request, from_station, to_station, journey_date):
    trains = Train.objects.filter(
        from_station__iexact=from_station,
        to_station__iexact=to_station,
        date=journey_date,
        available_seats__gt=0
    )

    return render(request, 'booking/trains_list.html', {
        'trains': trains,
        'from_station': from_station,
        'to_station': to_station,
        'journey_date': journey_date
    })

@login_required
def book_train_view(request, train_id, journey_date):
    train = get_object_or_404(Train, id=train_id, date=journey_date)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            seats_requested = form.cleaned_data['seats_booked']
            
            if seats_requested > train.available_seats:
                messages.error(request, "Not enough seats available!")
                return redirect('trains_list', from_station=train.from_station, to_station=train.to_station, journey_date=journey_date)

            # Create booking
            Booking.objects.create(
                user=request.user,
                train=train,
                date_of_journey=journey_date,
                seats_booked=seats_requested,
                status='CONFIRMED'
            )

            # Update available seats
            train.available_seats -= seats_requested
            train.save()

            messages.success(request, "Booking confirmed successfully!")
            return redirect('my_bookings')  # (You can create this page later)

    else:
        form = BookingForm()

    return render(request, 'booking/book_train.html', {'form': form, 'train': train, 'journey_date': journey_date})

