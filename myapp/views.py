from django.shortcuts import render, redirect
from .models import Hostel
from django.contrib.auth.hashers import make_password , check_password
from .models import HostelUser
from django.contrib.auth import authenticate, login , logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Import csrf_exempt decorator
from .models import Booking, Room
from django.utils import timezone 
from .models import Room ,Booking

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'About_us.html')


def contact(request):
    return render(request, 'Contact_us.html')



def hostels(request):
    hostels = Hostel.objects.all()
    return render(request, 'hostels.html', {'hostels': hostels})
def room_list(request, hostel_id):
    rooms = Room.objects.filter(HostelID=hostel_id)
    context = {'rooms': rooms}
    return render(request, 'room_list.html', context)

def signup(request):
    template_name = 'signup.html'

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        try:
            # Check if the user already exists
            existing_user = HostelUser.objects.get(Email=email)
            return render(request, template_name, {'error': 'User with this email already exists'})

        except HostelUser.DoesNotExist:
            # User does not exist, proceed with registration
            if password == confirm_password:
                hashed_password = make_password(password)
                user = HostelUser.objects.create(
                    Username=f"{first_name} {last_name}",
                    Email=email,
                    Password=hashed_password,
                    Usertype='Regular'
                )
                user.save()
                return redirect('login_view')  # Redirect to login page after successful registration
            else:
                # Passwords do not match, handle this case as needed
                pass

    return render(request, template_name)
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Bypass authenticate and query user directly
        user = HostelUser.objects.get(Email=email)

        if check_password(password, user.Password):
            # Passwords match, log in the user
            login(request, user)
            request.session['user_id'] = user.UserID  # Store user ID in session
            request.session['user_username'] = user.Username
            return render(request, 'home.html', {'user': user})
        else:
            return render(request, 'login.html', {'error': 'Incorrect password'})
    
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    request.session.clear()  # Clear the session
    return render(request, 'logout.html')
    # views.py

@csrf_exempt  # Apply csrf_exempt to allow POST requests without CSRF token (for simplicity in this example)
def book_now_view(request):
    if request.method == 'POST':
        # Extract data from the POST request
        room_id = request.POST.get('room_id')  # Assuming the room_id is sent in the POST request
        current_date = timezone.now().date()
        user_id = int(request.POST.get('user_id'))  # Assuming the USER_ID is sent in the POST request
        user = HostelUser.objects.get(pk=user_id)

        # Retrieve the Room instance
        room = Room.objects.get(pk=room_id)

        # Create a Booking instance
        booking = Booking(
            HostelUserID=user,  # Assuming you are using Django's built-in User model
            RoomID=room,
            BookingDate=current_date,
            TotalPrice=room.Price  # Replace with the actual calculation of total price
        )

        # Save the booking to the database
        booking.save()

        # Return a JSON response indicating success
        return JsonResponse({'status': 'success', 'booking_id': booking.BookingID})
    else:
        # Return a JSON response indicating an error
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
