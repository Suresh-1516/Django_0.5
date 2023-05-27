from django.db import models
 
class Profile(models.Model):
    profile_id = models.AutoField
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name

class Save_code(models.Model):
    file_id = models.AutoField
    file_user = models.CharField(max_length=100,default="")
    file_name = models.CharField(max_length=20)
    file_date = models.DateField()
    file_content = models.TextField(max_length=1000)

    def __str__(self):
        return self.file_name

class Premium(models.Model):
    premium_id = models.AutoField
    premium_name = models.CharField(max_length=20,default="")
    premium_amount = models.IntegerField(default=000)
    premium_img = models.ImageField(upload_to='premium/images',default="") 
    premium_date = models.DateField(default="")

    def __str__(self):
        return self.premium_name

class htmlquestion(models.Model):
    htmlqno = models.AutoField
    qchar = models.CharField(max_length=100,default="")
    wo1 = models.CharField(max_length=20,default="")
    wo2 = models.CharField(max_length=20,default="")
    wo3 = models.CharField(max_length=20,default="")
    wo4 = models.CharField(max_length=20,default="")
    ro = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.qchar


class Data(models.Model):

    user = models.CharField(max_length=20,default="") 
    premium_name = models.CharField(max_length=20,default="Nope")
    order_id = models.CharField(max_length=20,default="")
    email = models.EmailField(default="Nope")
    amount = models.IntegerField(default=0)
    mobileno = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class Doubt(models.Model):

    doubt_id = models.AutoField
    doubt_user = models.CharField(max_length=20,default="") 
    doubt_lang = models.CharField(max_length=50,default="")
    doubt_q = models.CharField(max_length=30,default="")
    doubt_code = models.CharField(max_length=1000,default="")
    
    def __str__(self):
        return self.doubt_lang

class Feedback(models.Model):

    feedback_id = models.AutoField
    feedback_user = models.CharField(max_length=20,default="")
    feedback_user_email = models.EmailField(default=None) 
    feedback_content = models.CharField(max_length=800,default="")
    feedback_rate = models.CharField(max_length=10,default=None)

    def __str__(self):
        return self.feedback_user

class Payment(models.Model):

    payment_id = models.AutoField
    payment_user = models.CharField(max_length=20,default="")
    name = models.CharField(max_length=30,default=None)
    enrolled_course= models.CharField(max_length=30,default=None)
    enrolled_id= models.CharField(max_length=30,default=None)
    mobile_no = models.IntegerField(default=None)
    email = models.EmailField(default=None)
    order_id = models.CharField(max_length=30,default=None)
    amount = models.IntegerField(default=None)

    def __str__(self):
        return self.payment_user
    
class Notes(models.Model):

    note_id = models.AutoField
    note_user = models.CharField(max_length=50,default=None)
    note_1 = models.CharField(max_length=400,default=None)
    note_2 = models.CharField(max_length=400,default=None)
    note_3 = models.CharField(max_length=400,default=None)

    def __str__(self):
        return self.note_user
    
