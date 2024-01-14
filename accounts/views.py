from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in !!!!")
            return redirect('dashboard')
        
        messages.error(request, "Invalid Credentials")
    return render(request, 'accounts/login.html')

# def login(request):
#     return render(request, 'accounts/login.html')


# def register(request):
#     return render(request, 'accounts/register.html')

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        isUsername = False
        isEmail = False

        if password == confirm_password:
            # user already in database
            if User.objects.filter(username=username).exists():
                isUsername = True
                messages.error(request, "Username already exists !!!")
                return redirect('register')
            
            # email already exists
            if User.objects.filter(email=email).exists():
                isEmail = True
                if isEmail and isUsername:
                    messages.error(request, "Email and username already exists, redirecting you to login !!!")
                    return redirect('login')

                messages.error(request, "Email already exists !!!")
                return redirect('register')


            user = User.objects.create_user(first_name = firstname,
                                           last_name = lastname,
                                           username = username,
                                           email = email,
                                           password = password)
            user.save()
            messages.success(request, "You are successfully registered !!!")
            return redirect('login')
        else:
            messages.error(request, "Passwords didn't match !!!")
            return redirect('register')

    return render(request, 'accounts/register.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/dashboard.html')
    messages.error(request, "You are not allowed to access this page !!!")
    return redirect('login')

# def logout(request):
#     auth.logout(request)
#     messages.success(request, "You are now logged out successfully !!!")
#     return redirect('login')
