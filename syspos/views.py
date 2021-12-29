from django.db.models import query
from django.shortcuts import render
from.models import tbl_customer, tbl_user_types,tbl_user
import datetime,jwt
from.serializer import CustomerSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
#LOGIN VIEW
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        email = request.data['us_email']
        password = request.data['us_password']
        user = tbl_user.objects.filter(us_email = email, us_password= password).first()
        if user is None:
            raise AuthenticationFailed('User not found!')
        payload = {
            'id': user.us_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        print(token)
       
        response = Response()
        response.set_cookie(key = 'jwt', value = token, httponly = True)
        response.data = {
            'jwt': token
        }
        return response


#Customer Adding
class CreateCustomer(ListCreateAPIView):
    serializer_class=CustomerSerializer
    queryset=tbl_customer.objects.all()
#Edit Customer
class UpdateDeleteCustomer(RetrieveUpdateDestroyAPIView):
    serializer_class=CustomerSerializer
    queryset=tbl_customer.objects.filter(trash=False)
    def delete(self, request, *args, **kwargs):
        if tbl_customer.objects.get(pr_id=kwargs['pk'],trash=False):
            tbl_customer.objects.filter(pr_id=kwargs['pk']).update(trash=True)
            
            return Response({'Message': 'deleted'}) 
            

            
        else:
            return Response({'Message': 'no data found'})



