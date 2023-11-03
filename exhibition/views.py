from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponse, Http404

import json
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from .models import Year, Team, Member, Info, Photo
from .serializers import YearSerializer, TeamSerializer, MemberSerializer,InfoSerializer,PhotoSerializer


def main(request,year=11):
    #main에 접근했을때 제일 먼저 보이는 page가 11기 관련이도록
    try:
        year_str=str(year)
        year_obj=get_object_or_404(Year, year=year_str)
        teamlist=get_list_or_404(Team,year=year_obj)
        serializer=TeamSerializer(teamlist,many=True)
        return JsonResponse(serializer.data, safe = False, json_dumps_params={'ensure_ascii': False})

    except Team.DoesNotExist:
        return JsonResponse({'message': '해당 정보를 찾을 수 없습니다.'}, status=404)

def detail(request, year, team):
    try:
        year_str=str(year)
        year_obj=get_object_or_404(Year, year=year_str)
        teamlist=get_list_or_404(Team,year=year_obj)

        team_obj=None

        for team_check in teamlist:
            if team_check.team==team:
                team_obj=team_check

        photolist=Photo.objects.filter(team=team_obj)
        #memberlist=get_object_or_404(Member, team=team_obj)
        memberlist = Member.objects.filter(team=team_obj)

        photo_serializer=PhotoSerializer(photolist).data
        member_serializer=MemberSerializer(memberlist,many=True).data

        response_data={
            'photos': photo_serializer,
            'members':member_serializer,
        }

        return JsonResponse(response_data, safe = False)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
