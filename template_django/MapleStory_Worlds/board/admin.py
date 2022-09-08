from django.contrib import admin
from .models import Mission_1, Mission_2, Mission_3, Mission_4, Mission_5

class BoardMission_1(admin.ModelAdmin):
    list_display = (
        'user_id',
        'team_name',
        'team_members',
        'mission',
        'thumbnail_imagesrc1',
        'mission_imagesrc2',
        'mission_imagesrc3',
        'mission_imagesrc4',
        )
    search_fields = ('user_id','team_name')

class BoardMission_2(admin.ModelAdmin):
    list_display = (
        'user_id',
        'team_name',
        'team_members',
        'mission',
        'thumbnail_imagesrc1',
        'mission_imagesrc2',
        'mission_imagesrc3',
        'mission_imagesrc4',
        )
    search_fields = ('user_id','team_name')

class BoardMission_3(admin.ModelAdmin):
    list_display = (
        'user_id',
        'team_name',
        'team_members',
        'mission',
        'thumbnail_imagesrc1',
        'mission_imagesrc2',
        'mission_imagesrc3',
        'mission_imagesrc4',
        )
    search_fields = ('user_id','team_name')

class BoardMission_4(admin.ModelAdmin):
    list_display = (
        'user_id',
        'team_name',
        'team_members',
        'mission',
        'thumbnail_imagesrc1',
        'mission_imagesrc2',
        'mission_imagesrc3',
        'mission_imagesrc4',
        )
    search_fields = ('user_id','team_name')

class BoardMission_5(admin.ModelAdmin):
    list_display = (
        'user_id',
        'team_name',
        'team_members',
        'mission',
        'thumbnail_imagesrc1',
        'mission_imagesrc2',
        'mission_imagesrc3',
        'mission_imagesrc4',
        )
    search_fields = ('user_id','team_name')

admin.site.register(Mission_1, BoardMission_1)
admin.site.register(Mission_2, BoardMission_2)
admin.site.register(Mission_3, BoardMission_3)
admin.site.register(Mission_4, BoardMission_4)
admin.site.register(Mission_5, BoardMission_5)

