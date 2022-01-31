from django.db import models

# Create your models here.


class productdetails(models.Model):
    Product_id = models.AutoField
    Product_name = models.CharField(max_length=100)
    Product_desc = models.CharField(max_length=10000)
    category = models.CharField(max_length=50, default="")
    Sub_category = models.CharField(max_length=50, default="")
    Price = models.IntegerField(default=0)
    product_date = models.DateField()
    image = models.ImageField(upload_to="Shops/images", default="")
    quantities = models.IntegerField(default=0)
    def __str__(self):
        return self.Product_name


class Contact(models.Model):
    C_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    Phoneno = models.CharField(max_length=10)
    desc = models.CharField(max_length=500)


class Orders(models.Model):
    O_id = models.AutoField(primary_key=True)
    item_Json = models.CharField(max_length=5000)
    Name = models.CharField(max_length=50)
    Email_id = models.EmailField(max_length=100)
    Amount = models.IntegerField(default=0)
    Address = models.CharField(max_length=111)
    City = models.CharField(max_length=111)
    State = models.CharField(max_length=100)
    Zip_code = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=100, default="")


class Solution(models.Model):
    S_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    soultion = models.CharField(max_length=10000)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=10000)
    timeStamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "........"
