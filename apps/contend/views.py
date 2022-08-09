from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.

def ContendView(request):
    return render(request, 'contend/contend.html')

def RoomView(request, room_name):
    username = request.user.username
    room_details = Room.objects.get(room_name=room_name)
    return render(request, 'contend/conversations.html', {
        'username': username,
        'room_name': room_name,
        'room_details': room_details,
    })

def CheckView(request):
    username = request.POST.get('student_name')
    room_name = request.POST.get('student_id')

    if Room.objects.filter(room_name=room_name).exists():
        return redirect(reverse('conversations', kwargs={'room_name': room_name}), {
            "username": username
        })
    else:
        new_room = Room.objects.create(room_name=room_name)
        new_room.save()
        return redirect(reverse('conversations', kwargs={'room_name': room_name}))

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')
def getMessages(request, room):
    room_details = Room.objects.get(room_name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})