from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Thread, Message
from .serializers import UserSerializer, ThreadSerializer, MessageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    @action(detail=False, methods=['post'])
    def get_or_create_thread(self, request):
        user1_id = request.data.get('user1_id')
        user2_id = request.data.get('user2_id')

        # Check if thread already exists
        thread = Thread.objects.filter(participants__id=user1_id).filter(participants__id=user2_id).first()

        if thread:
            serializer = self.get_serializer(thread)
        else:
            user1 = User.objects.get(pk=user1_id)
            user2 = User.objects.get(pk=user2_id)
            thread = Thread.objects.create()
            thread.participants.add(user1)
            thread.participants.add(user2)
            serializer = self.get_serializer(thread)

        return Response(serializer.data)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        thread_id = self.request.query_params.get('thread_id', None)
        queryset = Message.objects.filter(thread__id=thread_id).order_by('-created')
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        thread = Thread.objects.get(pk=serializer.validated_data['thread'])
        serializer.save(sender=request.user)
        thread.updated = serializer.validated_data['
