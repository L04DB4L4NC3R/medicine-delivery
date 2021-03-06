from rest_framework import generics

from .models import Orders, User, Medicine, FileUpload, ChatLine
from .serializers import OrdersSerializer, UserSerializer, MedicineSerializer, FileSerializer, ChatLineSerializer
from rest_framework.decorators import api_view
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import parsers
from rest_framework import response
from rest_framework import status
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
import requests
import base64
import hashlib


class ListOrdersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrderView(APIView):

    """
    GET and POST orders at /order
    """

    def get(self, request):
        order = Orders.objects.all()

        param = request.GET.items()
        for i in param:
            if i[0] == 'user_id':
                order = Orders.objects.all().filter(user_id=i[1])
            elif i[0] == 'order_id':
                order = Orders.objects.all().filter(order_id=i[1])
            elif i[0] == 'status':
                order = Orders.objects.all().filter(status=i[1])

        serializer_class = OrdersSerializer(order, many=True)
        return Response(serializer_class.data)

    def post(self, request):

        order = request.data
        # Create an article from the above data
        serializer_class = OrdersSerializer(data=order)
        serializer_class.is_valid(raise_exception=True)
        order_saved = serializer_class.save()
        return Response({"success": "Order '{}' created successfully"
                         .format(order_saved.order_id)})


@api_view(['POST'])
def AddOrderView(request):

    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListMedicinesView(generics.ListAPIView):

    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


@api_view(['POST'])
def AddMedicineView(request):

    serializer = MedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

class ChatView(APIView):

    def get(self, request):
        sorted_msg = ChatLine.objects.all().order_by('timestamp')
        param = request.GET.items()
        for i in param:
            print(i)
            chat_msg = ChatLine.objects.all().filter(order_id=i[1])
            sorted_msg = chat_msg.order_by('timestamp')

        serializer_class = ChatLineSerializer(sorted_msg, many=True)
        return Response(serializer_class.data)

    def post(self, request):

        message = request.data
        serializer_class = ChatLineSerializer(data=message)
        if serializer_class.is_valid(raise_exception=True):
            message_saved = serializer_class.save()
        return Response({"success": "Message '{}' saved successfully"
                         .format(message_saved.msg_id)})


class Authen(APIView):

    # login
    def post(self, request):
        serializer = UserSerializer(data=request.body)
        serializer_class.is_valid(raise_exception=True)
        user = User.objects.filter(user_id=serializer.user_id)
        if user is None:
            return Response({"failure": "User DNE"},
                            status=status.HTTP_401_UNAUTHORIZED)

        m = hashlib.md5()
        m.update(serializer.password)
        if user.password != m.digest():
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user_id)
        return Response({"refresh": str(refresh),
                         "access": str(refresh.access_token)})
