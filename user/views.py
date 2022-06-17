from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth.hashers import make_password

from .models import User as UserModel
from .models import UserType as UserTypeModel

class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('data', '')
        real_password = make_password(password, salt=None, hasher='default')
        
        usertype = request.data.get('usertype')
        usertype = UserTypeModel.objects.get(type=usertype)
        
        user = UserModel.objects.filter(email=email)
        
        if not user:
            user = UserModel(email=email, password=real_password, user_type=usertype)
            user.save()
            return Response({"msg": "회원가입 성공!!"})
        
        return Response({"msg": "이미 가입한 유저입니다."})