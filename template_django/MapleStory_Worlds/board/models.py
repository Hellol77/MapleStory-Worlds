from django.db import models
from django.conf import settings
from .choice import *
from ckeditor.fields import RichTextField
import os

# Create your models here.
class Mission_1(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    group = models.CharField(choices=GROUP_CHOICES, max_length=6, verbose_name="그룹", null=True)
    team_name = models.CharField(max_length=17, verbose_name="팀명", blank=True, null=True)
    team_members = models.CharField(max_length=30, verbose_name="팀원", blank=True, null=True)
#    mission = models.TextField(max_length=600, verbose_name="미션설명", blank=True, null=True)
    mission = RichTextField(blank=True, null=True)
    end_date = models.DateField(auto_now_add=True, null=True)
    

#    thumbnail_imagesrc1 = models.CharField(max_length=80, verbose_name='이미지1 주소', blank=True, null=True)
#    mission_imagesrc2 = models.CharField(max_length=80, verbose_name='이미지2 주소', blank=True, null=True)
#    mission_imagesrc3 = models.CharField(max_length=80, verbose_name='이미지3 주소', blank=True, null=True)
#    mission_imagesrc4 = models.CharField(max_length=80, verbose_name='이미지4 주소', blank=True, null=True)
    image1 = models.ImageField(upload_to = "mission1_thumbnail/", null=True, blank=True)
    image2 = models.ImageField(upload_to = "mission1_image1/", null=True, blank=True)
    image3 = models.ImageField(upload_to = "mission1_image2/", null=True, blank=True)
    image4 = models.ImageField(upload_to = "mission1_image3/", null=True, blank=True)


    def __str__(self):
        return str(self.user_id)

    def delete(self, *args, **kargs):
        if self.image1:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image1.path))
        if self.image2:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image2.path))
        if self.image3:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image3.path))
        if self.image4:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image4.path))
        super(Mission_1, self).delete(*args, **kargs)

    class Meta:
        db_table = 'Mission_1'
        verbose_name = 'Mission_1'
        verbose_name_plural = 'Mission_1'

class Mission_2(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    group = models.CharField(choices=GROUP_CHOICES, max_length=6, verbose_name="그룹", null=True)
    team_name = models.CharField(max_length=17, verbose_name="팀명", blank=True, null=True)
    team_members = models.CharField(max_length=30, verbose_name="팀원", blank=True, null=True)
#    mission = models.TextField(max_length=600, verbose_name="미션설명", blank=True, null=True)
    mission = RichTextField(blank=True, null=True)
    end_date = models.DateField(auto_now_add=True, null=True)

#    thumbnail_imagesrc1 = models.CharField(max_length=80, verbose_name='이미지1 주소', blank=True, null=True)
#    mission_imagesrc2 = models.CharField(max_length=80, verbose_name='이미지2 주소', blank=True, null=True)
#    mission_imagesrc3 = models.CharField(max_length=80, verbose_name='이미지3 주소', blank=True, null=True)
#    mission_imagesrc4 = models.CharField(max_length=80, verbose_name='이미지4 주소', blank=True, null=True)

    image1 = models.ImageField(upload_to = "mission2_thumbnail/", null=True, blank=True)
    image2 = models.ImageField(upload_to = "mission2_image1/", null=True, blank=True)
    image3 = models.ImageField(upload_to = "mission2_image2/", null=True, blank=True)
    image4 = models.ImageField(upload_to = "mission2_image3/", null=True, blank=True)

    def __str__(self):
        return str(self.user_id)

    def delete(self, *args, **kargs):
        if self.image1:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image1.path))
        if self.image2:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image2.path))
        if self.image3:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image3.path))
        if self.image4:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image4.path))
        super(Mission_2, self).delete(*args, **kargs)

    class Meta:
        db_table = 'Mission_2'
        verbose_name = 'Mission_2'
        verbose_name_plural = 'Mission_2'

class Mission_3(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    group = models.CharField(choices=GROUP_CHOICES, max_length=6, verbose_name="그룹", null=True)
    team_name = models.CharField(max_length=17, verbose_name="팀명", blank=True, null=True)
    team_members = models.CharField(max_length=30, verbose_name="팀원", blank=True, null=True)
#    mission = models.TextField(max_length=600, verbose_name="미션설명", blank=True, null=True)
    mission = RichTextField(blank=True, null=True)
    end_date = models.DateField(auto_now_add=True, null=True)

#    thumbnail_imagesrc1 = models.CharField(max_length=80, verbose_name='이미지1 주소', blank=True, null=True)
#    mission_imagesrc2 = models.CharField(max_length=80, verbose_name='이미지2 주소', blank=True, null=True)
#    mission_imagesrc3 = models.CharField(max_length=80, verbose_name='이미지3 주소', blank=True, null=True)
#    mission_imagesrc4 = models.CharField(max_length=80, verbose_name='이미지4 주소', blank=True, null=True)

    image1 = models.ImageField(upload_to = "mission3_thumbnail/", null=True, blank=True)
    image2 = models.ImageField(upload_to = "mission3_image1/", null=True, blank=True)
    image3 = models.ImageField(upload_to = "mission3_image2/", null=True, blank=True)
    image4 = models.ImageField(upload_to = "mission3_image3/", null=True, blank=True)
    
    def __str__(self):
        return str(self.user_id)

    def delete(self, *args, **kargs):
        if self.image1:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image1.path))
        if self.image2:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image2.path))
        if self.image3:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image3.path))
        if self.image4:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image4.path))
        super(Mission_3, self).delete(*args, **kargs)

    class Meta:
        db_table = 'Mission_3'
        verbose_name = 'Mission_3'
        verbose_name_plural = 'Mission_3'

class Mission_4(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    group = models.CharField(choices=GROUP_CHOICES, max_length=6, verbose_name="그룹", null=True)
    team_name = models.CharField(max_length=17, verbose_name="팀명", blank=True, null=True)
    team_members = models.CharField(max_length=30, verbose_name="팀원", blank=True, null=True)
#    mission = models.TextField(max_length=600, verbose_name="미션설명", blank=True, null=True)
    mission = RichTextField(blank=True, null=True)
    end_date = models.DateField(auto_now_add=True, null=True)

#    thumbnail_imagesrc1 = models.CharField(max_length=80, verbose_name='이미지1 주소', blank=True, null=True)
#    mission_imagesrc2 = models.CharField(max_length=80, verbose_name='이미지2 주소', blank=True, null=True)
#    mission_imagesrc3 = models.CharField(max_length=80, verbose_name='이미지3 주소', blank=True, null=True)
#    mission_imagesrc4 = models.CharField(max_length=80, verbose_name='이미지4 주소', blank=True, null=True)


    image1 = models.ImageField(upload_to = "mission4_thumbnail/", null=True, blank=True)
    image2 = models.ImageField(upload_to = "mission4_image1/", null=True, blank=True)
    image3 = models.ImageField(upload_to = "mission4_image2/", null=True, blank=True)
    image4 = models.ImageField(upload_to = "mission4_image3/", null=True, blank=True)
    
    def __str__(self):
        return str(self.user_id)

    def delete(self, *args, **kargs):
        if self.image1:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image1.path))
        if self.image2:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image2.path))
        if self.image3:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image3.path))
        if self.image4:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image4.path))
        super(Mission_4, self).delete(*args, **kargs)

    class Meta:
        db_table = 'Mission_4'
        verbose_name = 'Mission_4'
        verbose_name_plural = 'Mission_4'

class Mission_5(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    group = models.CharField(choices=GROUP_CHOICES, max_length=6, verbose_name="그룹", null=True)
    team_name = models.CharField(max_length=17, verbose_name="팀명", blank=True, null=True)
    team_members = models.CharField(max_length=30, verbose_name="팀원", blank=True, null=True)
#    mission = models.TextField(max_length=600, verbose_name="미션설명", blank=True, null=True)
    mission = RichTextField(blank=True, null=True)
    end_date = models.DateField(auto_now_add=True, null=True)

#    thumbnail_imagesrc1 = models.CharField(max_length=80, verbose_name='이미지1 주소', blank=True, null=True)
#    mission_imagesrc2 = models.CharField(max_length=80, verbose_name='이미지2 주소', blank=True, null=True)
#    mission_imagesrc3 = models.CharField(max_length=80, verbose_name='이미지3 주소', blank=True, null=True)
#    mission_imagesrc4 = models.CharField(max_length=80, verbose_name='이미지4 주소', blank=True, null=True)

    image1 = models.ImageField(upload_to = "mission4_thumbnail/", null=True, blank=True)
    image2 = models.ImageField(upload_to = "mission4_image1/", null=True, blank=True)
    image3 = models.ImageField(upload_to = "mission4_image2/", null=True, blank=True)
    image4 = models.ImageField(upload_to = "mission4_image3/", null=True, blank=True)

    def __str__(self):
        return str(self.user_id)

    def delete(self, *args, **kargs):
        if self.image1:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image1.path))
        if self.image2:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image2.path))
        if self.image3:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image3.path))
        if self.image4:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image4.path))
        super(Mission_5, self).delete(*args, **kargs)

    class Meta:
        db_table = 'Mission_5'
        verbose_name = 'Mission_5'
        verbose_name_plural = 'Mission_5'