import base64
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import LoginSerializer, RegisterSerializer, ChangePasswordSerializer, VerifySerializer, generate_otp,\
    UserSerializer
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework import generics
from rest_framework.response import Response
from .models import User


class LoginView(TokenViewBase):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer


class VerifyView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = VerifySerializer

    def post(self, request):
        key = request.data.get('secret_key')
        secret = base64.b32decode(key)
        email = secret.decode()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response('user is not exists')

        otp = generate_otp(email)

        if request.data.get('otp') == otp.get('OTP'):
            user.isVerified = True
            user.save()
            refresh = TokenObtainPairSerializer.get_token(user)

            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data,
            }
            return Response(data)
        else:
            return Response('Wrong OTP')


class RegisterView(generics.CreateAPIView):
    # queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email=serializer.validated_data['email'])
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response({'msg': "password update successfully"})
