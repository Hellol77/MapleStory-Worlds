from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import LoginForm
from board.models import Mission_1, Mission_2, Mission_3, Mission_4, Mission_5
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, JsonResponse

# Create your views here.

from django.contrib.auth.hashers import make_password

def main_view(request):
    if request.user.is_authenticated:
        if Mission_1.objects.filter(user_id = request.user).exists():
            link1 = "/detail/M1/"+str(Mission_1.objects.filter(user_id = request.user)[0].id)
        else:
            link1="None"
        if Mission_2.objects.filter(user_id = request.user).exists():
            link2 = "/detail/M2/"+str(Mission_2.objects.filter(user_id = request.user)[0].id)
        else:
            link2="None"
        if Mission_3.objects.filter(user_id = request.user).exists():
            link3 = "/detail/M3/"+str(Mission_3.objects.filter(user_id = request.user)[0].id)
        else:
            link3="None"
        if Mission_4.objects.filter(user_id = request.user).exists():
            link4 = "/detail/M4/"+str(Mission_4.objects.filter(user_id = request.user)[0].id)
        else:
            link4="None"
        if Mission_5.objects.filter(user_id = request.user).exists():
            link5 = "/detail/M5/"+str(Mission_5.objects.filter(user_id = request.user)[0].id)
        else:
            link5="None"
    else:
        link1, link2, link3, link4, link5 = "None", "None", "None", "None", "None"
    context  = {
        "link1":link1,
        "link2":link2,
        "link3":link3,
        "link4":link4,
        "link5":link5,
    }
    a = "abcd"
    hashed_pass = make_password(a)
    print(hashed_pass)

    return render(request, 'users/index.html', context)

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

    def form_invalid(self, form: LoginForm):
        
        context={
        'login':'error',
        }
        
        return JsonResponse(context)



def logout_view(request):
    logout(request)
    return redirect('/')