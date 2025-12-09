from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import FeedBack, Customer

# Create your views here.
def index(request):
    return render(request, 'index.html')

# about view
def about(request):  
    return render(request, 'about.html')

# registration form view
def register(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate passwords
        if password != confirm_password:
            # Handle password mismatch error
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        # Create user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Create customer
        Customer.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address
        )

        return redirect('index')

    return render(request, 'register.html')

def book_service(request):
    return render(request, 'book.html')

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        rating = request.POST.get('rating')

        # Create and save feedback object
        FeedBack.objects.create(
            name=name,
            email=email,
            message=message,
            rating=rating
        )
        return redirect('index')
    return render(request, 'index.html')