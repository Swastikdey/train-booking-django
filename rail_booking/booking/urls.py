from django.urls import path
from . import views

#urlpatterns = [
#    path('', views.available_trains, name = 'home'),
#    path('book/<int:train_id>/', views.book_ticket, name='book_ticket'),
#    ]

urlpatterns = [
    path('search/', views.search_trains_view, name='search_trains'),
    path('trains_list/<str:from_station>/<str:to_station>/<str:journey_date>/', views.trains_list_view, name='trains_list'),
    path('book/<int:train_id>/<str:journey_date>/', views.book_train_view, name='book_train'),
    path('bookings/', views.my_bookings_view, name='my_bookings'),

]