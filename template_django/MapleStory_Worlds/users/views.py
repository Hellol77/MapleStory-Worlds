from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import LoginForm
from board.models import Mission_1, Mission_2, Mission_3, Mission_4, Mission_5
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from users.decorators import *
from django.utils.decorators import method_decorator

# Create your views here.

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

    mission1 = Mission_1.objects.order_by('-pk')[:4]
    for i in range(len(mission1)):
        if mission1[i].image1 == '':
            mission1[i].image1 = "/static/board/img/nothumnail.png"
        else:
            mission1[i].image1 = "/media/"+str(mission1[i].image1)

    mission2 = Mission_2.objects.order_by('-pk')[:4]
    for i in range(len(mission2)):
        if mission2[i].image1 == '':
            mission2[i].image1 = "/static/board/img/nothumnail.png"
        else:
            mission2[i].image1 = "/media/"+str(mission2[i].image1)

    mission3 = Mission_3.objects.order_by('-pk')[:4]
    for i in range(len(mission3)):
        if mission3[i].image1 == '':
            mission3[i].image1 = "/static/board/img/nothumnail.png"
        else:
            mission3[i].image1 = "/media/"+str(mission3[i].image1)

    mission4 = Mission_4.objects.order_by('-pk')[:4]
    for i in range(len(mission4)):
        if mission4[i].image1 == '':
            mission4[i].image1 = "/static/board/img/nothumnail.png"
        else:
            mission4[i].image1 = "/media/"+str(mission4[i].image1)

    mission5 = Mission_5.objects.order_by('-pk')[:4]
    for i in range(len(mission5)):
        if mission5[i].image1 == '':
            mission5[i].image1 = "/static/board/img/nothumnail.png"
        else:
            mission5[i].image1 = "/media/"+str(mission5[i].image1)

    context  = {
        "link1":link1,
        "link2":link2,
        "link3":link3,
        "link4":link4,
        "link5":link5,
        "mission1":mission1,
        "mission2":mission2,
        "mission3":mission3,
        "mission4":mission4,
        "mission5":mission5,
    }
    return render(request, 'users/index.html', context)

@method_decorator(logout_message_required, name='dispatch')
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
        messages.error(self.request, '아이디 비밀번호를 확인해주세요.')
        return super().form_invalid(form)



def logout_view(request):
    logout(request)
    return redirect('/')