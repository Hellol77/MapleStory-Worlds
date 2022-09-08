from django.db import models
from django.conf import settings
from .choice import *
from ckeditor.fields import RichTextField

# Create your models here.
class Mission_1(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    group = models.CharField(choices=GROUP_CHOICES, max_length=6, verbose_name="그룹", null=True)
    team_name = models.CharField(max_length=17, verbose_name="팀명", blank=True, null=True)
    team_members = models.CharField(max_length=30, verbose_name="팀원", blank=True, null=True)
#    mission = models.TextField(max_length=600, verbose_name="미션설명", blank=True, null=True)
    mission = RichTextField(blank=True, null=True)

    thumbnail_imagesrc1 = models.CharField(max_length=80, verbose_name='이미지1 주소', blank=True, null=True)
    mission_imagesrc2 = models.CharField(max_length=80, verbose_name='이미지2 주소', blank=True, null=True)
    mission_imagesrc3 = models.CharField(max_length=80, verbose_name='이미지3 주소', blank=True, null=True)
    mission_imagesrc4 = models.CharField(max_length=80, verbose_name='이미지4 주소', blank=True, null=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        db_table = 'Mission_1'
        verbose_name = 'Mission_1'
        verbose_name_plural = 'Mission_1'

class Mission_2(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    group = models.CharField(choices=GROUP_CHOICES, max_length=6, verbose_name="그룹", null=True)
    team_name = models.CharField(max_length=17, verbose_name="팀명", blank=True, null=True)
    team_members = models.CharField(max_length=30, verbose_name="팀원", blank=True, null=True)
    mission = models.TextField(max_length=600, verbose_name="미션설명", blank=True, null=True)

    thumbnail_imagesrc1 = models.CharField(max_length=80, verbose_name='이미지1 주소', blank=True, null=True)
    mission_imagesrc2 = models.CharField(max_length=80, verbose_name='이미지2 주소', blank=True, null=True)
    mission_imagesrc3 = models.CharField(max_length=80, verbose_name='이미지3 주소', blank=True, null=True)
    mission_imagesrc4 = models.CharField(max_length=80, verbose_name='이미지4 주소', blank=True, null=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        db_table = 'Mission_2'
        verbose_name = 'Mission_2'
        verbose_name_plural = 'Mission_2'

class Mission_3(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    group = models.CharField(choices=GROUP_CHOICES, max_length=6, verbose_name="그룹", null=True)
    team_name = models.CharField(max_length=17, verbose_name="팀명", blank=True, null=True)
    team_members = models.CharField(max_length=30, verbose_name="팀원", blank=True, null=True)
    mission = models.TextField(max_length=600, verbose_name="미션설명", blank=True, null=True)

    thumbnail_imagesrc1 = models.CharField(max_length=80, verbose_name='이미지1 주소', blank=True, null=True)
    mission_imagesrc2 = models.CharField(max_length=80, verbose_name='이미지2 주소', blank=True, null=True)
    mission_imagesrc3 = models.CharField(max_length=80, verbose_name='이미지3 주소', blank=True, null=True)
    mission_imagesrc4 = models.CharField(max_length=80, verbose_name='이미지4 주소', blank=True, null=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        db_table = 'Mission_3'
        verbose_name = 'Mission_3'
        verbose_name_plural = 'Mission_3'

class Mission_4(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    group = models.CharField(choices=GROUP_CHOICES, max_length=6, verbose_name="그룹", null=True)
    team_name = models.CharField(max_length=17, verbose_name="팀명", blank=True, null=True)
    team_members = models.CharField(max_length=30, verbose_name="팀원", blank=True, null=True)
    mission = models.TextField(max_length=600, verbose_name="미션설명", blank=True, null=True)

    thumbnail_imagesrc1 = models.CharField(max_length=80, verbose_name='이미지1 주소', blank=True, null=True)
    mission_imagesrc2 = models.CharField(max_length=80, verbose_name='이미지2 주소', blank=True, null=True)
    mission_imagesrc3 = models.CharField(max_length=80, verbose_name='이미지3 주소', blank=True, null=True)
    mission_imagesrc4 = models.CharField(max_length=80, verbose_name='이미지4 주소', blank=True, null=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        db_table = 'Mission_4'
        verbose_name = 'Mission_4'
        verbose_name_plural = 'Mission_4'

class Mission_5(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    group = models.CharField(choices=GROUP_CHOICES, max_length=6, verbose_name="그룹", null=True)
    team_name = models.CharField(max_length=17, verbose_name="팀명", blank=True, null=True)
    team_members = models.CharField(max_length=30, verbose_name="팀원", blank=True, null=True)
    mission = models.TextField(max_length=600, verbose_name="미션설명", blank=True, null=True)

    thumbnail_imagesrc1 = models.CharField(max_length=80, verbose_name='이미지1 주소', blank=True, null=True)
    mission_imagesrc2 = models.CharField(max_length=80, verbose_name='이미지2 주소', blank=True, null=True)
    mission_imagesrc3 = models.CharField(max_length=80, verbose_name='이미지3 주소', blank=True, null=True)
    mission_imagesrc4 = models.CharField(max_length=80, verbose_name='이미지4 주소', blank=True, null=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        db_table = 'Mission_5'
        verbose_name = 'Mission_5'
        verbose_name_plural = 'Mission_5'