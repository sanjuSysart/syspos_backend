from django.db import models
from phone_field import PhoneField

#USERTYPES
class tbl_user_types(models.Model):
    id=models.AutoField(primary_key=True)
    create_date=models.DateTimeField(auto_now=True)
    type_name=models.CharField(max_length=250)
    trash=models.BooleanField(default=False)
    def __str__(self):
        return self.type_name
#USERS
class tbl_user(models.Model):
    us_id=models.AutoField(primary_key=True)
    us_name=models.CharField(max_length=300)
    us_email=models.EmailField(max_length=300)
    us_password=models.CharField(max_length=300)
    us_type=models.CharField(max_length=100)
    us_image=models.ImageField(upload_to='images', blank=True, null=True)
    trash=models.BooleanField(default=False)

    USERNAME_FIELD = 'us_email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
            return self.us_name


#CUSTOMER TABLE
class tbl_customer(models.Model):
    cus_id=models.AutoField(primary_key=True)
    cus_join_date=models.DateTimeField(auto_now=True)
    cus_name=models.CharField(max_length=300,null=True)
    cus_email=models.EmailField(max_length=300,null=True)
    cus_mobile=PhoneField(null=True)
    cus_address=models.TextField(null=True)
    cus_user=models.IntegerField()
    cus_loyalty=models.BooleanField(default=True)
    trash=models.BooleanField(default=True)
    def __str__(self):
            return self.cus_name


#PRODUCT TABLE 



