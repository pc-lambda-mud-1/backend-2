from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def welcome(request):
  content = { 'message': 'Welcome to our MUD Game'}
  return JsonResponse(content, status=200)