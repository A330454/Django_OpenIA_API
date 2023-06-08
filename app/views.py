from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .openai_utils import gpt3_request
import json

# Create your views here.

# def gpt3_view(request):
#     prompt = request.GET.get('prompt', '')
#     response = gpt3_request(prompt)
#     return JsonResponse({'response': response})

@csrf_exempt
def gpt3_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content', '')
        response = gpt3_request(content)
        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)