from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# get flash messages
from .forms import UserRegisterForm


# Create your views here.


def register(request):
    """
    1) check for what type of request
    2) display a the imported sign up form
    3) if the for is valid -> flash message -> redirect
    4) else display a new blank form
    """
    """
    The forms have some built-in invalid feedback
    """
    if request.method == "POST":
        if request.method == 'POST':
            # 1) form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        # display an empty form if not POST request
        # 1) form = UserCreationForm()
        form = UserRegisterForm()
        # messages.success(request, "Try Again!")
    return render(request, 'users/register.html', {'form': form})
