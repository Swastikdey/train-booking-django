from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, CustomLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! 🎉")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = CustomLoginForm  # Use Django's built-in if you didn't customize
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, "✅ Successfully logged in.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')

def custom_logout(request):
    logout(request)
    messages.info(request, "✅ You have been logged out successfully.")
    return redirect('login')


'''
DEBUG	debug	gray
INFO	info	blue
SUCCESS	success	green
WARNING	warning	yellow/orange
ERROR	error	red
'''