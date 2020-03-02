from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def welcome(request):
  content = { 'message': 'Welcome to our MUD Game'}
  return JsonResponse(content)