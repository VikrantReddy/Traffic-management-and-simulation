from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

# Create your views here.


@api_view(["POST"])
def GetMaps(map_number):
    j_file = open("maps.json")
    map_content = json.load(j_file)
    try:
        print(map_number)
        number = str(json.loads(map_number.body))
        resp = map_content[number]

        return JsonResponse(resp, safe=False)
    except ValueError as error:
        return Response(error.args[0], status.HTTP_400_BAD_REQUEST)

    j_file.close()
