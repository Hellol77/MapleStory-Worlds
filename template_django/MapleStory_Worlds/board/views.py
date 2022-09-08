from django.shortcuts import render,redirect
from .models import Mission_1, Mission_2, Mission_3, Mission_4, Mission_5
from django.core.paginator import Paginator
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def PostUpload(request):
    if request.method == 'POST':
        team_name = request.POST['team_name']
        team_members = request.POST['team_members']
        mission = request.POST['mission']

        request_dictionary = {"1": Mission_1, "2": Mission_2, "3": Mission_3, "4": Mission_4, "5": Mission_5}
        requestModel = request_dictionary.get(request.POST["show"])

        postupload = requestModel(
                user_id = request.user,
                team_name=team_name,
                team_members=team_members,
                mission=mission,
                group=request.user.group
            )
        postupload.save()
        return redirect('/')

    else:
        group = request.user.group
        context = {
                "group": group,
            }
        return render(request, 'board/register.html', context)

def DetailView(request):
    return render(request, 'board/check.html')

def mission_show(request):
    input_val = request.GET.get('input_val')
    request_dictionary = {"1": Mission_1, "2": Mission_2, "3": Mission_3, "4": Mission_4, "5": Mission_5}
    requestModel = request_dictionary.get(input_val)
    listall = requestModel.objects.filter(group="A")
    num = len(listall)

    team_name = []
    team_members = []
    thumbnail_imagesrc1 = []


    for i in range(num):
        team_name.append(listall[i].team_name)
        team_members.append(listall[i].team_members)
        thumbnail_imagesrc1.append(listall[i].thumbnail_imagesrc1)

    context={
        'num':num,
        'team_name' : team_name,
        'team_members' : team_members,
        'thumbnail_imagesrc1' : thumbnail_imagesrc1,
        }
    print(context)
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


    for i in range(num):
        team_name.append(listall[i].team_name)
        team_members.append(listall[i].team_members)
        thumbnail_imagesrc1.append(listall[i].thumbnail_imagesrc1)

    context={
        'num':num,
        'team_name' : team_name,
        'team_members' : team_members,
        'thumbnail_imagesrc1' : thumbnail_imagesrc1,
        }

    return JsonResponse(context)