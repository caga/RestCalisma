from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from sineppets.models import Snippet
from snippets.serializers import SnippetSerializer
# Create your views here.

# @csref_exempt 
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method=='GET':
#         snippets=Snippet.objects.all()
#         serializer=SnippetSerializer(sni

