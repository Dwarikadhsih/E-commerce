from django.db import models

# Create your models here.
class Blogdetails(models.Model):
    Post_id = models.AutoField
    Title = models.CharField(max_length=100)
    heading0 = models.CharField(max_length=10000, default="")
    dheading0 = models.CharField(max_length=10000, default="")
    heading1 = models.CharField(max_length=50000, default="")
    dheading1 = models.CharField(max_length=10000, default="")
    heading2 = models.CharField(max_length=10000, default="")
    dheading2 = models.CharField(max_length=50000, default="")
    Blog_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="Shops/images", default="")

    def __str__(self):
        return self.Title
