from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http.response import JsonResponse
from rest_framework import status
from datetime import datetime
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
# Create your views here.
@api_view(['GET'])
def EventsapiOverView(request):
    api_urls={
        'List':'/eventsList/',
        'Detail View': '/eventsList/<int:id>/',
        'Update':'/eventsUpdate/<int:id>',
        'Create':'/eventsCreate/',
        'Delete':'/eventsDelete/<int:id>/'
    }
    return Response(api_urls)



@api_view(['GET'])
@permission_classes((IsAdminUser, ))
def getEventsDetails(request):
    getevents=Events.objects.all()
    evS=eventSerializer(getevents,many=True)
    return Response(evS.data,status=status.HTTP_200_OK)
@api_view(['GET'])
def getUpcomingEvents(request):
    current_time = datetime.now()
    getevents=Events.objects.filter(startDate__gte=datetime.now())
    evS=eventSerializer(getevents,many=True)
    return Response(evS.data,status=status.HTTP_200_OK)
# @api_view(['GET'])
# def getEventsByLocation(request,emp_id):
#     baselocation=UserDetails.objects.get(emp_id=emp_id).base_location
    # result=Events.objects.all()
    # print(result)
    # evS=eventSerializer(result,many=True)
    # empids=[]
    # locations=[]
    # for empId in evS.data:
    #     print(empId["adminEmpId"])
    #     empids.append(empId["adminEmpId"])
    # for empid in empids:
    #     result1=UserDetails.objects.filter(emp_id=empid)
    #     print(result1[0])
    # # eventsByLocation=Events.objects.filter(adminEmpId__baselocation=baselocation)
    # # evS=eventSerializer(eventsByLocation,many=True)
    # print(baselocation)
    # return Response(evS.data,status=status.HTTP_200_OK)
    # result=Events.objects.filter(baselocation=baselocation)
    # evS=eventSerializer(result,many=True)
    # return Response(evS.data,status=status.HTTP_200_OK)
    

@api_view(['POST'])
def createEvents(request):
    serializer=eventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def deleteEvents(request,pk):
    try:
        event=Events.objects.get(pk=pk)
    except Events.DoesNotExist:
        return Response("event doesnot exist",status=status.HTTP_404_NOT_FOUND)
    event.delete()
    return Response("event is deleted successfully")

@api_view(['PATCH'])
def updateEvents(request,pk):
    try:
        event=Events.objects.get(pk=pk)
    except Events.DoesNotExist:
        return Response("event doesnot exist",status=status.HTTP_404_NOT_FOUND)
    serializer = eventSerializer(event, data=request.data, partial=True) # set partial=True to update a data partially
    if serializer.is_valid():
            serializer.save()
            return Response("Sucessfully Updated")
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

##################  event types api ##########################

@api_view(['GET'])
def getEventTypes(request):
    geteventTypes=EventTypes.objects.all()
    serializer=eventTypesSerializer(geteventTypes,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def getEventTypes(request,pk):
    geteventTypesById=EventTypes.objects.filter(pk=pk)
    serializer=eventTypesSerializer(geteventTypesById,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

##################  workshops api ##########################
@api_view(['GET'])
def getWorkshops(request):
    getworkshops=Workshops.objects.all()
    serializer=WorkshopsSerializer(getworkshops,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['GET'])
def getUpcomingWorkshops(request):
    getevents=Events.objects.filter(startDate__gte=datetime.now())
    serializer=WorkshopsSerializer(getevents,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def createWorkshops(request):
    data=request.data
    event_obj=Events.objects.get(eventName=data["eventName"])
    eventType_obj=EventTypes.objects.get(eventType=data["eventType"]) 
    newWorkshop=Workshops.objects.create(
        workshopName=data["workshopName"],
        objectives=data["objectives"],
        contentDetails=data["contentDetails"],
        requirements=data["requirements"],
        instructorId=data["instructorId"],
        poster=request.FILES["poster"],
        startDate=data["startDate"],
        endDate=data["endDate"],
        venue=data["venue"],
        prerequisites=data["prerequisites"],
        instructorName=data["instructorName"],
        experience=data["experience"],
        skills=data["skills"],
        instructorDesignation=data["instructiorDesignation"],
        instructorProfilePic=request.FILES["instructorProfilePic"],
        eventType=eventType_obj,
        event=event_obj
    )
    newWorkshop.save() 
    serializer=WorkshopsSerializer(newWorkshop)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['DELETE','PATCH'])
def deleteAndUpdateWorkshops(request,pk):
    
    try:
        workshop=Workshops.objects.get(pk=pk)
    except Workshops.DoesNotExist:
        return Response("workshop doesnot exist",status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
    
        workshop.delete()
        return Response("workshop is deleted successfully")
    elif request.method == 'PATCH' :
        serializer = WorkshopsSerializer(workshop, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response("Sucessfully Updated")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
#################################### SPORTS ##############################################
@api_view(['GET'])
def getSports(request):
    getSports=Sports.objects.all()
    serializer=SportsSerializer(getSports,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def createSports(request):
    data=request.data
    event_obj=Events.objects.get(eventName=data["eventName"])
    eventType_obj=EventTypes.objects.get(eventType=data["eventType"]) 
    newSport=Sports.objects.create(
        sportName=data["sportName"],
        sportType=data["sportType"],
        team=data["Team"],
        teamSize=data["TeamSize"],
        eventType=eventType_obj,
        event=event_obj,
        sportsDetails=data["sportsDetails"]
    )
    time=TimeLines.objects.create(startDate=data["startDate"],endDate=data["endDate"],venue=data["venue"],poster=request.FILES["poster"],
                                  sports=newSport)
    newSport.save() 
    serializer=SportsSerializer(newSport)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['PATCH','DELETE'])
def deleteAndUpdateSports(request,pk):
    try:
        sports=Sports.objects.get(pk=pk)
    except Sports.DoesNotExist:
        return Response("sport doesnot exist",status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
    
        sports.delete()
        return Response("sport is deleted successfully")
    elif request.method == 'PATCH' :
        serializer = SportsSerializer(sports, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response("Sucessfully Updated")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

############################## employee wellness ############################################

@api_view(['GET'])
def get(request):
    getEmployeeWellnessEvents=Sports.objects.all()
    serializer=EmployeeWellnessSerializer(getEmployeeWellnessEvents,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

########################### sending mails ###########################

@api_view(['GET'])
def send_mail_plain_with_file(request):
    message="hi this is rasagjna"
    subject="example mail"
    mail_id="mailtorasagjna201000@gmail.com"
    email=EmailMessage(subject,message,settings.EMAIL_HOST_USER,[mail_id])
    email.content_subtype = "html"
    # file=open("example.txt","r")
    # email.attach("example.txt",file.read(),'text/plain')
    email.send()
    return Response("email sent successfully")

############################### reading files ##########################


@api_view(['POST'])
def readfiles(request):
    serializer=MyfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getfile(request,pk):
    getfile=ExampleFiles.objects.get(pk=pk)
    serializer=MyfileSerializer(getfile)
    return Response(serializer.data,status=status.HTTP_200_OK)

################################# Hackathon ###############

    
@api_view(['GET'])
def getHackathons(request,pk):
    hackathons=Hackathon.objects.all()
    serializer=HackathonSerializer(hackathons,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','PATCH','DELETE'])
def getbyIdAnddeleteAndUpdateHackathons(request,pk):
    try:
        hackathons=Hackathon.objects.get(pk=pk)
    except Hackathon.DoesNotExist:
        return Response("hackathon doesnot exist",status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=HackathonSerializer(hackathons)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        hackathons.delete()
        return Response("hackathon is deleted successfully")
    elif request.method == 'PATCH' :
        serializer = HackathonSerializer(hackathons, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response("Sucessfully Updated")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

######################### ART #################################

@api_view(['GET'])
def getArts(request,pk):
    arts=Arts.objects.all()
    serializer=ArtsSerializer(Arts,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','PATCH','DELETE'])
def getbyIdAnddeleteAndUpdateArts(request,pk):
    try:
        arts=Arts.objects.get(pk=pk)
    except Arts.DoesNotExist:
        return Response("art doesnot exist",status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=ArtsSerializer(arts)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        arts.delete()
        return Response("art is deleted successfully")
    elif request.method == 'PATCH' :
        serializer = ArtsSerializer(arts, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response("Sucessfully Updated")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
##################################### timelines ##################################################

@api_view(['GET'])
def getTimeLines(request,pk):
    dateAndTime=TimeLines.objects.all()
    serializer=TimeLines(dateAndTime,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','PATCH','DELETE'])
def getbyIdAnddeleteAndUpdateDate(request,pk):
    try:
        timelines=TimeLines.objects.get(pk=pk)
    except TimeLines.DoesNotExist:
        return Response("dateAndTime doesnot exist",status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=TimeLinesSerializer(timelines)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        timelines.delete()
        return Response("dateAndTime is deleted successfully")
    elif request.method == 'PATCH' :
        serializer = TimeLinesSerializer(timelines, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response("Sucessfully Updated")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
############################## ORGANIZERS ################################

@api_view(['GET'])
def getOrganizers(request):
    organizers=Organizers.objects.all()
    serializer=TimeLines(organizers,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def getOrganizers(request):
    serializer=OrganizersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
############################# user sign in #####################
class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
    
    
    






      





        

        
   
            
    
    

