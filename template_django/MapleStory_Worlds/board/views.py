from django.shortcuts import render,redirect, get_object_or_404
from .models import Mission_1, Mission_2, Mission_3, Mission_4, Mission_5
from .forms import PostForm_1, PostForm_2, PostForm_3, PostForm_4, PostForm_5
from django.http import JsonResponse

# Create your views here.
def PostUpload(request):
    if request.method == 'POST':
        team_name = request.POST['team_name']
        team_members = request.POST['team_members']
        mission = request.POST['mission']
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')

        request_dictionary = {"1": Mission_1, "2": Mission_2, "3": Mission_3, "4": Mission_4, "5": Mission_5}
        requestModel = request_dictionary.get(request.POST["show"])

        postupload = requestModel(
                user_id = request.user,
                team_name=team_name,
                team_members=team_members,
                mission=mission,
                group=request.user.group,
                image1=image1,
                image2=image2,
                image3=image3,
                image4=image4,
            )
        postupload.save()
        return redirect('/')

    else:
        group = request.user.group
        
        userM1 = Mission_1.objects.filter(user_id = request.user).exists()
        userM2 = Mission_2.objects.filter(user_id = request.user).exists()
        userM3 = Mission_3.objects.filter(user_id = request.user).exists()
        userM4 = Mission_4.objects.filter(user_id = request.user).exists()
        userM5 = Mission_5.objects.filter(user_id = request.user).exists()

        context = {
                "group": group,
                "userM1": userM1,
                "userM2": userM2,
                "userM3": userM3,
                "userM4": userM4,
                "userM5": userM5,
            }
        return render(request, 'board/register.html', context)

def CheckView(request):
    return render(request, 'board/check.html')



def DetailView_M1(request,pk):
    pagepk = get_object_or_404(Mission_1, pk=pk)
    missionTag = "M1"

    if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
        edit_auth= True
    else:
        edit_auth=False

    if Mission_1.objects.filter(pk__lt=pk).order_by('-pk').first() == None and Mission_1.objects.filter(pk__gt=pk).order_by('-pk').first() == None:
        the_prev = pk
        the_next = pk
    else:
        try:
            the_prev = Mission_1.objects.filter(pk__lt=pk).order_by('-pk').first().pk
        except:
            the_prev = Mission_1.objects.filter(pk__gt=pk).order_by('-pk').first().pk
        try:
            the_next = Mission_1.objects.filter(pk__gt=pk).order_by('pk').first().pk
        except:
            the_next = Mission_1.objects.filter(pk__lt=pk).order_by('pk').first().pk

    context = {
        "pk" : pk,
        "tag" : missionTag,
        "team_name" : pagepk.team_name,
        "team_members" : pagepk.team_members,
        "mission" : pagepk.mission,
        "end_date" : pagepk.end_date,
        "edit_auth" : edit_auth,
        "the_prev" : the_prev,
        "the_next" : the_next,
    }
    return render(request, 'board/detail.html', context)

def DetailView_M2(request,pk):
    pagepk = get_object_or_404(Mission_2, pk=pk)
    missionTag = "M2"

    if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
        edit_auth= True
    else:
        edit_auth=False

    if Mission_2.objects.filter(pk__lt=pk).order_by('-pk').first() == None and Mission_2.objects.filter(pk__gt=pk).order_by('-pk').first() == None:
        the_prev = pk
        the_next = pk
    else:
        try:
            the_prev = Mission_2.objects.filter(pk__lt=pk).order_by('-pk').first().pk
        except:
            the_prev = Mission_2.objects.filter(pk__gt=pk).order_by('-pk').first().pk
        try:
            the_next = Mission_2.objects.filter(pk__gt=pk).order_by('pk').first().pk
        except:
            the_next = Mission_2.objects.filter(pk__lt=pk).order_by('pk').first().pk

    context = {
        "pk" : pk,
        "tag" : missionTag,
        "team_name" : pagepk.team_name,
        "team_members" : pagepk.team_members,
        "mission" : pagepk.mission,
        "end_date" : pagepk.end_date,
        "edit_auth" : edit_auth,
        "the_prev" : the_prev,
        "the_next" : the_next,
    }
    return render(request, 'board/detail.html', context)

def DetailView_M3(request,pk):
    pagepk = get_object_or_404(Mission_3, pk=pk)
    missionTag = "M3"

    if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
        edit_auth= True
    else:
        edit_auth=False
    
    if Mission_3.objects.filter(pk__lt=pk).order_by('-pk').first() == None and Mission_3.objects.filter(pk__gt=pk).order_by('-pk').first() == None:
        the_prev = pk
        the_next = pk
    else:
        try:
            the_prev = Mission_3.objects.filter(pk__lt=pk).order_by('-pk').first().pk
        except:
            the_prev = Mission_3.objects.filter(pk__gt=pk).order_by('-pk').first().pk
        try:
            the_next = Mission_3.objects.filter(pk__gt=pk).order_by('pk').first().pk
        except:
            the_next = Mission_3.objects.filter(pk__lt=pk).order_by('pk').first().pk

    context = {
        "pk" : pk,
        "tag" : missionTag,
        "team_name" : pagepk.team_name,
        "team_members" : pagepk.team_members,
        "mission" : pagepk.mission,
        "end_date" : pagepk.end_date,
        "edit_auth" : edit_auth,
        "the_prev" : the_prev,
        "the_next" : the_next,
    }
    return render(request, 'board/detail.html', context)

def DetailView_M4(request,pk):
    pagepk = get_object_or_404(Mission_4, pk=pk)
    missionTag = "M4"

    if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
        edit_auth= True
    else:
        edit_auth=False
    
    if Mission_4.objects.filter(pk__lt=pk).order_by('-pk').first() == None and Mission_4.objects.filter(pk__gt=pk).order_by('-pk').first() == None:
        the_prev = pk
        the_next = pk
    else:
        try:
            the_prev = Mission_4.objects.filter(pk__lt=pk).order_by('-pk').first().pk
        except:
            the_prev = Mission_4.objects.filter(pk__gt=pk).order_by('-pk').first().pk
        try:
            the_next = Mission_4.objects.filter(pk__gt=pk).order_by('pk').first().pk
        except:
            the_next = Mission_4.objects.filter(pk__lt=pk).order_by('pk').first().pk

    context = {
        "pk" : pk,
        "tag" : missionTag,
        "team_name" : pagepk.team_name,
        "team_members" : pagepk.team_members,
        "mission" : pagepk.mission,
        "end_date" : pagepk.end_date,
        "edit_auth" : edit_auth,
        "the_prev" : the_prev,
        "the_next" : the_next,
    }
    return render(request, 'board/detail.html', context)

def DetailView_M5(request,pk):
    pagepk = get_object_or_404(Mission_5, pk=pk)
    missionTag = "M5"

    if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
        edit_auth= True
    else:
        edit_auth=False
    
    if Mission_5.objects.filter(pk__lt=pk).order_by('-pk').first() == None and Mission_5.objects.filter(pk__gt=pk).order_by('-pk').first() == None:
        the_prev = pk
        the_next = pk
    else:
        try:
            the_prev = Mission_5.objects.filter(pk__lt=pk).order_by('-pk').first().pk
        except:
            the_prev = Mission_5.objects.filter(pk__gt=pk).order_by('-pk').first().pk
        try:
            the_next = Mission_5.objects.filter(pk__gt=pk).order_by('pk').first().pk
        except:
            the_next = Mission_5.objects.filter(pk__lt=pk).order_by('pk').first().pk

    context = {
        "pk" : pk,
        "tag" : missionTag,
        "team_name" : pagepk.team_name,
        "team_members" : pagepk.team_members,
        "mission" : pagepk.mission,
        "end_date" : pagepk.end_date,
        "edit_auth" : edit_auth,
        "the_prev" : the_prev,
        "the_next" : the_next,
    }
    return render(request, 'board/detail.html', context)


def mission_show(request):
    input_val = request.GET.get('input_val')
    request_dictionary = {"1": Mission_1, "2": Mission_2, "3": Mission_3, "4": Mission_4, "5": Mission_5}
    requestModel = request_dictionary.get(input_val)
    listall = requestModel.objects.filter(group="A")
    num = len(listall)

    team_name = []
    team_members = []
    thumbnail_imagesrc1 = []
    page_src = []


    for i in range(num):
        team_name.append(listall[i].team_name)
        team_members.append(listall[i].team_members)
        if listall[i].image1 == '':
            thumbnail_imagesrc1.append("/static/board/img/nothumnail.png")
        else:
            thumbnail_imagesrc1.append(str(listall[i].image1))
        page_src.append('/detail/M'+input_val+'/'+str(listall[i].id))

    context={
        'num':num,
        'team_name' : team_name,
        'team_members' : team_members,
        'thumbnail_imagesrc1' : thumbnail_imagesrc1,
        'page_src' : page_src,
        }

    return JsonResponse(context)

def mission_show_semi(request):
    input_val = request.GET.get('input_val')
    input_val_at = request.GET.get('input_val_at')
    request_dictionary = {"1": Mission_1, "2": Mission_2, "3": Mission_3, "4": Mission_4, "5": Mission_5}
    requestModel = request_dictionary.get(input_val)
    listall = requestModel.objects.filter(group=input_val_at)
    num = len(listall)

    team_name = []
    team_members = []
    thumbnail_imagesrc1 = []
    page_src = []


    for i in range(num):
        team_name.append(listall[i].team_name)
        team_members.append(listall[i].team_members)
        if listall[i].image1 == '':
            thumbnail_imagesrc1.append("/static/board/img/nothumnail.png")
        else:
            thumbnail_imagesrc1.append(str(listall[i].image1))
        page_src.append('/detail/M'+input_val+'/'+str(listall[i].id))

    context={
        'num':num,
        'team_name' : team_name,
        'team_members' : team_members,
        'thumbnail_imagesrc1' : thumbnail_imagesrc1,
        'page_src' : page_src,
        }

    return JsonResponse(context)

def mission_delete_M1(request, pk):
    pagepk = get_object_or_404(Mission_1, pk=pk)
    if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
        pagepk.delete()
        return redirect('/check')
    else:
        return redirect('/check')

def mission_delete_M2(request, pk):
    pagepk = get_object_or_404(Mission_2, pk=pk)
    if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
        pagepk.delete()
        return redirect('/check')
    else:
        return redirect('/check')

def mission_delete_M3(request, pk):
    pagepk = get_object_or_404(Mission_3, pk=pk)
    if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
        pagepk.delete()
        return redirect('/check')
    else:
        return redirect('/check')

def mission_delete_M4(request, pk):
    pagepk = get_object_or_404(Mission_4, pk=pk)
    if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
        pagepk.delete()
        return redirect('/check')
    else:
        return redirect('/check')

def mission_delete_M5(request, pk):
    pagepk = get_object_or_404(Mission_5, pk=pk)
    if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
        pagepk.delete()
        return redirect('/check')
    else:
        return redirect('/check')



def mission_edit_M1(request, pk):
    pagepk = get_object_or_404(Mission_1, pk=pk)
    if request.method == "POST":
        if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
            form = PostForm_1(request.POST, request.FILES, instance=pagepk)
            if form.is_valid():
                pagepk = form.save(commit = False)
                pagepk.save()
                return redirect('/detail/M1/'+str(pk))

    else:
        if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
            context = {
                'team_name' : pagepk.team_name,
                'team_members' : pagepk.team_members,
                'mission' : pagepk.mission
            }
            return render(request, "board/register.html", context)
        else:
            return redirect('/')

def mission_edit_M2(request, pk):
    pagepk = get_object_or_404(Mission_2, pk=pk)
    if request.method == "POST":
        if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
            form = PostForm_2(request.POST, request.FILES, instance=pagepk)
            if form.is_valid():
                pagepk = form.save(commit = False)
                pagepk.save()
                return redirect('/detail/M2/'+str(pk))

    else:
        if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
            context = {
                'team_name' : pagepk.team_name,
                'team_members' : pagepk.team_members,
                'mission' : pagepk.mission
            }
            return render(request, "board/register.html", context)
        else:
            return redirect('/')

def mission_edit_M3(request, pk):
    pagepk = get_object_or_404(Mission_3, pk=pk)
    if request.method == "POST":
        if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
            form = PostForm_3(request.POST, request.FILES, instance=pagepk)
            if form.is_valid():
                pagepk = form.save(commit = False)
                pagepk.save()
                return redirect('/detail/M3/'+str(pk))

    else:
        if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
            context = {
                'team_name' : pagepk.team_name,
                'team_members' : pagepk.team_members,
                'mission' : pagepk.mission
            }
            return render(request, "board/register.html", context)
        else:
            return redirect('/')

def mission_edit_M4(request, pk):
    pagepk = get_object_or_404(Mission_4, pk=pk)
    if request.method == "POST":
        if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
            form = PostForm_4(request.POST, request.FILES, instance=pagepk)
            if form.is_valid():
                pagepk = form.save(commit = False)
                pagepk.save()
                return redirect('/detail/M4/'+str(pk))

    else:
        if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
            context = {
                'team_name' : pagepk.team_name,
                'team_members' : pagepk.team_members,
                'mission' : pagepk.mission
            }
            return render(request, "board/register.html", context)
        else:
            return redirect('/')

def mission_edit_M5(request, pk):
    pagepk = get_object_or_404(Mission_5, pk=pk)
    if request.method == "POST":
        if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
            form = PostForm_5(request.POST, request.FILES, instance=pagepk)
            if form.is_valid():
                pagepk = form.save(commit = False)
                pagepk.save()
                return redirect('/detail/M5/'+str(pk))

    else:
        if pagepk.user_id == request.user or request.user.level == '0' or request.user.level == '1':
            context = {
                'team_name' : pagepk.team_name,
                'team_members' : pagepk.team_members,
                'mission' : pagepk.mission
            }
            return render(request, "board/register.html", context)
        else:
            return redirect('/')
    