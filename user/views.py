from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from Admin.models import Service
from .models import FeedBack, Customer

# Create your views here.
def index(request):
   services = Service.objects.filter(active=True).order_by('name')
   return render(request, 'index.html', {'services': services})

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

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')  # Redirect to the homepage on successful login
        else:
            error = 'Invalid username or password. Please try again.'
    
    return render(request, 'login.html', {'error': error})

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('index')


def book_service(request):
    return render(request, 'book.html')

def feedback_list(request):
    """Render a list of all feedback entries."""
    feedback = FeedBack.objects.all().order_by('-id')
    return render(request, 'feedback.html', {'feedback': feedback})

@require_POST
def submit_feedback(request):
    """Handle the submission of the feedback form. Only accepts POST."""
    name = request.POST.get('name')
    email = request.POST.get('email')
    service_id = request.POST.get('service')
    message = request.POST.get('message')
    rating = request.POST.get('rating')

    service = None
    if service_id:
        try:
            service = Service.objects.get(pk=service_id)
        except (Service.DoesNotExist, ValueError):
            # Handle case where service_id is invalid, maybe log it
            service = None

    FeedBack.objects.create(
        name=name,
        email=email,
        service=service,
        message=message,
        rating=rating
    )
    return redirect('index')
