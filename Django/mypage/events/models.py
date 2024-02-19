from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
# Create your models here.
# Create your models here.
# class UserDetails(models.Model):
#     emp_id=models.IntegerField(primary_key=True,default=123)
#     first_name=models.CharField(max_length=150,null=False,blank=False,default='Batikiri')
#     last_name=models.CharField(max_length=150,null=False,blank=False,default='ANU')
#     email=models.EmailField(unique=True)
#     password=models.CharField(max_length=30)
#     mobile=models.CharField(max_length=10)
#     designation=models.CharField(max_length=200,null=False,blank=False,default="Engineer")
#     bu=models.CharField(max_length=250,null=True)
#     role=models.CharField(max_length=150,default="user")
#     base_location=models.CharField(max_length=150,null=False,blank=False,default='none')
#     blood_group=models.CharField(max_length=10,null=True,blank=True)
#     profile_pic=models.ImageField(upload_to='uploads/images', null=True, blank=True)
#     gender=models.CharField(max_length=30,null=True,blank=True,default="Null")
#     def __str__(self):
#         return self.email+" - "+str(self.emp_id)
    
########################################################## abstract user table ###############################


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_name=models.CharField(max_length=150,null=False,blank=False,default='ANU')
    mobile=models.CharField(max_length=10)
    designation=models.CharField(max_length=200,null=False,blank=False,default="Engineer")
    bu=models.CharField(max_length=250,null=True)
    role=models.CharField(max_length=150,default="user")
    base_location=models.CharField(max_length=150,null=False,blank=False,default='none')
    blood_group=models.CharField(max_length=10,null=True,blank=True)
    profile_pic=models.ImageField(upload_to='uploads/images', null=True, blank=True)
    gender=models.CharField(max_length=30,null=True,blank=True,default="Null")
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name','last_name']

    def __str__(self):
        return self.user_name



###########################################################################################################
class Events(models.Model):
    eventName=models.CharField(max_length=150, null=False, blank=False)
    startDate=models.DateTimeField(auto_now=False, auto_now_add=False)
    endDate=models.DateTimeField(auto_now=False, auto_now_add=False)
    venue=models.CharField( max_length=150,null=False, blank=False)
    poster=models.ImageField(upload_to='uploads/images', null=True, blank=True)
    adminEmpId= models.IntegerField(null=False, blank=False,default=123)
    baselocation=models.CharField(max_length=150,null=False, blank=False)
    theme=models.CharField( max_length=150,null=False, blank=False)
    def __str__(self):
        return self.eventName
class EventTypes(models.Model):
    eventType=models.CharField(max_length=150, null=False, blank=False,default="NoNe")
    events=models.ManyToManyField(Events,related_name="events")
    def __str__(self):
        return self.eventType
class Hackathon(models.Model):

    hackathon_name=models.CharField(max_length=150,null=False,blank=False)

    startDate=models.DateTimeField(auto_now=False, auto_now_add=False)

    endDate=models.DateTimeField(auto_now=False, auto_now_add=False)

    poster=models.ImageField(upload_to='uploads/images', null=True, blank=True)

    hackathon_details=models.TextField(default="Details about Hackathon")

    venue=models.CharField(max_length=150,null=False,blank=False)

    eventType= models.ForeignKey(EventTypes,on_delete = models.CASCADE,null=True,blank=True)

    event= models.ForeignKey(Events,on_delete = models.CASCADE,null=True,blank=True)



    def __str__(self):

        return self.hackathon_name


class Workshops(models.Model):
    workshopName=models.CharField(max_length=150,null=False,blank=False)
    objectives=models.CharField(max_length=150,null=False,blank=False)
    contentDetails= models.TextField(null=False,blank=False)
    requirements= models.CharField(max_length=150,null=False,blank=False)
    instructorId=models.IntegerField(null=False,blank=False)
    poster=models.ImageField(upload_to='uploads/images', null=True, blank=True)
    startDate=models.DateTimeField(auto_now=False, auto_now_add=False)
    endDate=models.DateTimeField(auto_now=False, auto_now_add=False)
    venue=models.CharField(max_length=150,null=False,blank=False)
    prerequisites=models.CharField(max_length=150,null=False,blank=False)
    instructorName= models.CharField(max_length=150,null=False,blank=False)
    experience=models.IntegerField(null=False,blank=False)
    skills=models.TextField(null=False,blank=False)
    instructorDesignation=models.CharField(max_length=150,null=False,blank=False,default="Software Engineer")
    instructorProfilepic=models.ImageField(upload_to='uploads/images', null=True, blank=True)
    eventType= models.ForeignKey(EventTypes,on_delete = models.CASCADE)
    event= models.ForeignKey(Events,on_delete = models.CASCADE)
    def __str__(self):
        return self.workshopName
####################  COMMON TABLE #################################################



class Sports(models.Model):

    sportName=models.CharField(max_length=150,null=False,blank=False)

    sportType=models.CharField(max_length=150,null=False,blank=False)

    team=models.BooleanField()

    sportsDetails=models.TextField(default="Enter details about sports")

    teamSize=models.IntegerField(null=False,blank=False)

    eventType= models.ForeignKey(EventTypes,on_delete = models.CASCADE,null=True,blank=True)

    event= models.ForeignKey(Events,on_delete = models.CASCADE,null=True,blank=True)



    def __str__(self):

        return self.sportName

class EmployeeWellness(models.Model):
    ewName=models.CharField(max_length=150,null=False,blank=False)
    wellnessType=models.CharField(max_length=150,null=False,blank=False,default="employee wellness")
    EWDetails = models.TextField(null=False,blank=False)
    eventType= models.ForeignKey(EventTypes,on_delete = models.CASCADE,null=True,blank=True)
    event= models.ForeignKey(Events,on_delete = models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.ewName
class TimeLines(models.Model):
    startDate= models.DateTimeField(auto_now=False, auto_now_add=False)
    endDate=models.DateTimeField(auto_now=False, auto_now_add=False)
    venue= models.CharField(max_length=150,null=False,blank=False)
    poster=models.ImageField(upload_to='uploads/images', null=True, blank=True)
    sports=models.ForeignKey(Sports,on_delete = models.CASCADE,null=True,blank=True)
    employeeWellness=models.ForeignKey(EmployeeWellness,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return  self.venue


class Donations(models.Model):
    donationTo=models.CharField(max_length=150,null=False,blank=False)
    minAmount=models.FloatField(max_length=150,null=False,blank=False)
    totalAmount=models.FloatField(max_length=150,null=False,blank=False)
    startDate=models.DateTimeField(auto_now=False, auto_now_add=False)
    endDate=models.DateTimeField(auto_now=False, auto_now_add=False)
    poster=models.ImageField(upload_to='uploads/images', null=True, blank=True)
    donationDetails= models.FileField(upload_to='uploads/files',null=False, blank=False)
    Socialwellness= models.ForeignKey(EventTypes,on_delete = models.CASCADE)
    wellnessType=models.CharField(max_length=150,null=False,blank=False,default="social wellness")
    def __str__(self):
        return self.donationTo
class UserDonation(models.Model):
    empId= models.IntegerField(null=False,blank=False)
    donatedAmount = models.FloatField(max_length=150,null=False,blank=False)
    donation=models.ForeignKey(Donations,on_delete = models.CASCADE)
    def __str__(self):
        return self.empId
    
class Arts(models.Model):

    artName=models.CharField(max_length=150)

    artType=models.CharField(max_length=150)

    theme=models.CharField(max_length=150)

    arts_details=models.TextField(default="Details about Arts")

    eventType=models.ForeignKey(EventTypes,on_delete = models.CASCADE,null=True,blank=True)

    event= models.ForeignKey(Events,on_delete = models.CASCADE,null=True,blank=True)

    def __str__(self):

        return self.artName
    
class Organizers(models.Model):
    status=models.BooleanField(default=False)
    empId=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True,blank=True)
    eventId= models.ForeignKey(Events,on_delete = models.CASCADE,null=True,blank=True)
    def __str__(self):

        return self.empId
    
class ExampleFiles(models.Model):
    file=models.FileField(upload_to='uploads/images', null=False, blank=True)
    
    
    
    
    
    

    
    



    
    
    
    
    
    
    
    
    



