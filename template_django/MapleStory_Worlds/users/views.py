from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def main_view(request):
    return render(request, 'users/index.html')

class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=user_id, password=password)
        
        if user is not None:
            self.request.session['user_id'] = user_id
            login(self.request, user)

        return super().form_valid(form)

def logout_view(request):
    logout(request)
    return redirect('/')