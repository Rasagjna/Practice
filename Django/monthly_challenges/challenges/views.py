
from turtle import forward
from urllib import response
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import Http404,HttpResponseRedirect,HttpResponseNotFound,HttpResponse
# Create your views here.
# def january(request):
#     return HttpResponse("This works!")
# def february(request):
#     return HttpResponse("this is february month")
# def march(request):
#     return HttpResponse("this is march month")
monthly_challenges= {
    "january":"this is jan",
    "february":"this is feb",
    "march":"this is march",
    "april":"this is april",
    "may":"this is may",
    "june":"this is june",
    "july":"this is july",
    "august":"this is august",
    "september":"this is sep",
    "october":"this is oct",
    "november":"this is nov",
    "december":None,

}
def index(request):
    # list_items =""
    months=list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months":months
    })
    # for month in months:
    #     capitalized_month=month.capitalize()
    #     month_path=reverse("month-challenge",args=[month])
    #     list_items+= f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    #     # "<li><a href="...">January</a> </li><li><a href="...">February</a></li>..."
    # response_data=f"<ul>{list_items}</ul>"
    
    # return HttpResponse(response_data)

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month]) #/challenge/january
    # return HttpResponseRedirect("/challenges/"+redirect_month)
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        text=monthly_challenges[month]
        # response_data = f"<h1>{text}</h2>"
        return render(request,"challenges/challenge.html",{
            "text":text,
            "month_name":month

        })
        # response_data=render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # return render(request,"404.html")
        raise Http404()
        # return HttpResponseNotFound("<h1>this month is not supported!</h1>")
   

