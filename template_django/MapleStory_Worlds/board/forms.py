from django import forms
from .models import Mission_1, Mission_2, Mission_3, Mission_4
from ckeditor.widgets import CKEditorWidget

class PostForm_1(forms.ModelForm):
    team_name = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '팀명을 입력해주세요.'},
        max_length=17,
        label='팀명'
    )
    team_members = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '팀원을 입력해주세요.'},
        max_length=40,
        label='팀원'
    )
#    mission = forms.CharField(
#        widget=forms.TextInput(
#        attrs={'class': 'form-control',}), 
#        error_messages={'required': '미션설명을 입력해주세요.'},
#        max_length=600,
#        label='미션설명'
#    )
    mission = forms.CharField(
        widget=CKEditorWidget(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '미션설명을 입력해주세요.'},
        max_length=600,
        label='미션설명'
    )

    class Meta:
        model = Mission_1
        fields = ['team_name', 'team_members', 'mission', 'mission1_imagesrc1', 'mission1_imagesrc2','mission1_imagesrc3','mission1_imagesrc4']


class PostForm_2(forms.ModelForm):
    team_name = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '팀명을 입력해주세요.'},
        max_length=17,
        label='팀명'
    )
    team_members = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '팀원을 입력해주세요.'},
        max_length=40,
        label='팀원'
    )
    mission = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '미션설명을 입력해주세요.'},
        max_length=600,
        label='미션설명'
    )
    class Meta:
        model = Mission_2
        fields = ['team_name', 'team_members', 'mission', 'mission2_imagesrc1', 'mission2_imagesrc2','mission2_imagesrc3','mission2_imagesrc4']



class PostForm_3(forms.ModelForm):
    team_name = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '팀명을 입력해주세요.'},
        max_length=17,
        label='팀명'
    )
    team_members = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '팀원을 입력해주세요.'},
        max_length=40,
        label='팀원'
    )
    mission = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '미션설명을 입력해주세요.'},
        max_length=600,
        label='미션설명'
    )
    class Meta:
        model = Mission_3
        fields = ['team_name', 'team_members', 'mission', 'mission3_imagesrc1', 'mission3_imagesrc2','mission3_imagesrc3','mission3_imagesrc4']



class PostForm_1(forms.ModelForm):
    team_name = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '팀명을 입력해주세요.'},
        max_length=17,
        label='팀명'
    )
    team_members = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '팀원을 입력해주세요.'},
        max_length=40,
        label='팀원'
    )
    mission = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        error_messages={'required': '미션설명을 입력해주세요.'},
        max_length=600,
        label='미션설명'
    )
    class Meta:
        model = Mission_4
        fields = ['team_name', 'team_members', 'mission', 'mission4_imagesrc1', 'mission4_imagesrc2','mission4_imagesrc3','mission4_imagesrc4']
