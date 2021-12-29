from rest_framework import serializers
from.models import tbl_customer



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=tbl_customer
        fields="__all__"