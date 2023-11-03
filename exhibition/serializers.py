from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Year, Team, Member, Info, Photo

class YearSerializer(ModelSerializer):
    class Meta:
        model = Year
        fields = ['year']

class TeamSerializer(ModelSerializer):
    year = YearSerializer()
    class Meta:
        model = Team
        fields = ['year', 'team', 'p_name']

class MemberSerializer(ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Member
        fields = ['team','name','m_id','major']

class InfoSerializer(ModelSerializer):
    team = TeamSerializer()
    madeby = MemberSerializer()
    class Meta:
        model = Info
        fields = ['team','madeby']

class PhotoSerializer(ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Photo
        fields = ['team', 'index', 'photo']