# Add 'get_object_or_404' to your imports at the top
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # Built-in form
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm # Built-in Login Form

# ... your other views (product_list, product_detail) ...


# Create your views here.

from .models import Product

def product_list(request):
    # This gets all products from your database
    products = Product.objects.all()
    # This sends those products to an HTML file called index.html
    return render(request, 'shop/index.html', {'products': products})
# NEW FUNCTION:
def product_detail(request, pk):
    # This finds the product by its ID (pk) or shows a 404 error if not found
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/detail.html', {'product': product})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
             try:
               form.save() # Saves the new user to the database
               username = form.cleaned_data.get('username')
               messages.success(request, f'Account created for {username}! You can now log in.')
               return redirect('login') # take them to login-page
             except Exception as e: 
                messages.error(request,"An error occurred during registration. Please try a different username")
    
                
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('product_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('product_list')
