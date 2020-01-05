from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Real_estate, MyUserManager, MyUser, Like, Message
from .serializer import CateSerializer, RS_Serializer, RS_detail_Serializer, Message_Serializer

class CateViewSet(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        queryset = Category.objects.all()
        serializer = CateSerializer(queryset, many=True)
        return Response(serializer.data)

class RS_ViewSet(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        queryset = Real_estate.objects.all()
        serializer = RS_Serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        new_name = request.data['name']
        new_detail = request.data['detail']
        new_image = reqeust.data['image']
        new_price = request.data['price']
        new_category = request.data['category']

class LandMark(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        queryset = Real_estate.objects.filter(category__name="랜드마크")
        serializer = RS_Serializer(queryset, many=True)
        return Response(serializer.data)

class Residential(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        queryset = Real_estate.objects.filter(category__name="주거용")
        serializer = RS_Serializer(queryset, many=True)
        return Response(serializer.data)

class Commercial(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        queryset = Real_estate.objects.filter(category__name="상업용")
        serializer = RS_Serializer(queryset, many=True)
        return Response(serializer.data)

class Detail(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, id, format=None):
        queryset = Real_estate.objects.get(id = id)
        serializer = RS_detail_Serializer(queryset, many=False)
        return Response(serializer.data)

class Signup(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, format=None):
        if MyUser.objects.filter(email=request.data['username']).count()>=1:
            return Response("email Error")
        else:
            email = request.data['username']
            name = request.data['nickname']
            password = request.data['password']
            MyUser.objects.create_user(email=email, name=name, password=password)
            return Response(email)

class Recommand(APIView):
    def post(self, request, id, format=None):
        queryset = Real_estate.objects.get(id = id)
        user_email= request.data['username']
        user = MyUser.objects.get(email= user_email)
        Recommand_object = Like.objects.filter(user=user, realestate_post=queryset)
        if Recommand_object.count()>=1:
            Recommand_object.delete()
        else:
            Like.objects.create(user=user, realestate_post=queryset)
        queryset.likecount = Like.objects.filter(realestate_post=queryset).count()
        print(queryset.likecount)
        queryset.save()
        return Response("success")

class Message_view(APIView):

    def get(self, request, format=None):
        user = request.headers['Username']
        queryset_receiver = Message.objects.filter(receiver__email=user)
        queryset_sender = Message.objects.filter(sender__email=user)
        queryset_total = queryset_receiver | queryset_sender
        queryset_total.order_by('-send_time')
        queryset_total.order_by('-recent_msg')
        serializer = Message_Serializer(queryset_total, many=True)
        print(queryset_total)
        return Response(serializer.data)

class RecentMessage(APIView):

    def get(self, request, format=None):
        user = request.headers['Username']
        queryset_receiver = Message.objects.filter(receiver__email=user, recent_msg=True)
        queryset_sender = Message.objects.filter(sender__email=user, recent_msg=True)
        queryset_total = queryset_receiver | queryset_sender
        serializer = Message_Serializer(queryset_total, many=True)
        return Response(serializer.data)

class DetailMessageView(APIView):
    def get(self, request, id, format=None):
        user = request.headers['Username']
        queryset_receiver = Message.objects.filter(receiver__email=user, real_estate__id=id)
        queryset_sender = Message.objects.filter(sender__email=user, real_estate__id=id)
        queryset_total = (queryset_receiver | queryset_sender).order_by('-send_time')
        serializer = Message_Serializer(queryset_total, many=True)
        return Response(serializer.data)

    def post(self,request, id, format=None):

        input_email_user = request.headers['Username']
        input_email_receiver = request.data['receiver'][0]

        user = MyUser.objects.get(email=input_email_user)
        message = request.data['message']
        receiver = MyUser.objects.get(email=input_email_receiver)

        real_estate = Real_estate.objects.get(id=id)

        msg_sent = Message.objects.filter(real_estate=real_estate, sender=user, receiver=receiver, recent_msg=True)
        msg_received = Message.objects.filter(real_estate=real_estate, sender=receiver, receiver=user, recent_msg=True)
        msg_total = msg_sent | msg_received

        new_msg = Message(
            sender=user,
            receiver=receiver,
            message=message,
            real_estate=real_estate,
        )

        new_msg.save()

        for msg in msg_total:
            print(msg.recent_msg)
            msg.recent_msg = False
            msg.save()
        new_msg.recent_msg = True
        new_msg.save()
        return Response("complete")


class MessageReceiver(APIView):
    def get(self, request, id, format=None):
        user = request.headers['Username']
        queryset_receiver = Message.objects.filter(receiver__email=user, real_estate__id=id)
        queryset_sender = Message.objects.filter(sender__email=user, real_estate__id=id)
        queryset_total = queryset_receiver | queryset_sender
        real_estate_owner = Real_estate.objects.get(id=id).owner.email
        init_message_user = []

        if real_estate_owner != user:
            init_message_user.append(real_estate_owner)

        else:
            pass

        for queryset in queryset_total:
            if queryset.sender.email != user:
                init_message_user.append(queryset.sender.email)
            else:
                pass
            if queryset.receiver.email != user:
                init_message_user.append(queryset.receiver.email)
            else:
                pass
        message_user = list(set(init_message_user))
        return Response(message_user)
