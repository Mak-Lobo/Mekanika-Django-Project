from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

# about view
def about(request):  
    return render(request, 'about.html')

# registration form view
def register(request):
    return render(request, 'register.html')

def book_service(request):
    return render(request, 'book.html')
