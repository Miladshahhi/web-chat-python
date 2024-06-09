from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import User, Message
import json

def index(request):
    return render(request, 'chat/index.html')

def messages(request):
    messages = Message.objects.all().order_by('timestamp')
    return JsonResponse(list(messages.values('user__username', 'content', 'timestamp')), safe=False)

def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        content = data.get('content')
        if username and content:
            user, created = User.objects.get_or_create(username=username)
            Message.objects.create(user=user, content=content)
            return JsonResponse({'status': 'success'})
        return HttpResponseBadRequest('Invalid data')
    return HttpResponseBadRequest('Only POST method allowed')
