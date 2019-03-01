from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
import random
# Create your views here.
def index(request):
    a = [1,2,3,4]
    random_num = random.choice(a)
    return render(request, 'chat_app/index.html', {'random_num':random_num})

def room(request, room_name):
    return render(request, 'chat_app/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })