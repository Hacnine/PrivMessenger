from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import User
import jwt, datetime


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']

            user = User.objects.filter(username=username).first()

            if user is None:
                raise AuthenticationFailed('User not found!')

            if not user.check_password(password):
                raise AuthenticationFailed('Incorrect password!')

            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')

            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'jwt': token
            }
            return response
        except Exception as e:
            return Response({"error": str(e)}, status=500)


# class LoginView(APIView):
#     def post(self, request):
#         username = request.data['username']
#         passmessage = request.data['passmessage']
#         password = request.data['password']
#         user = User.objects.filter(username=username).first()
#
#         if user is None:
#             raise AuthenticationFailed('User not found')
#         if user.passmessage != passmessage:
#             raise AuthenticationFailed('Incorrect Pass Message')
#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect Password')
#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }
#         token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token
#         }
#         return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Un Authenticated')
        user = User.objects.filter(id=payload['id']).first()
        return Response(token)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'log out'
        }
        return response
