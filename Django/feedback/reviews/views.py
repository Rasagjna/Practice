from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView

import reviews

# Create your views here.
from .forms import ReviewForm
from .models import Review


class ReviewView(CreateView):
    model=Review
    form_class= ReviewForm
    template_name = "reviews/reviews.html"
    success_url = "/thank-you"


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/reviews.html"
#     success_url = "/thank-you"
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)



# class ReviewView(View):
#     def get(self,request):
#         form=ReviewForm()
#         return render(request,"reviews/reviews.html",{
#         # "has_error":False
#         "form":form
#     })

#     def post(self,request):
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request,"reviews/reviews.html",{
#         # "has_error":False
#         "form":form
#     })
     
def review(request):
    if request.method == 'POST':
        # existing_model=Review.objects.get(pk=1)
        # form=ReviewForm(request.POST,instance=existing_model)
        form=ReviewForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # review=Review(
            #     user_name = form.cleaned_data['user_name'],
            #     review_text=form.cleaned_data['review_text'],
            #     rating=form.cleaned_data['rating']
            # )
            # review.save()
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form=ReviewForm()
        
    #     entered_username= request.POST['username']
    #     if entered_username=="":
    #          return render(request,"reviews/review.html",{
    #             "has_error":True
    #          })
            
    #     print(entered_username)
    #     return HttpResponseRedirect("/thank-you")
    # form=ReviewForm()
    return render(request,"reviews/review.html",{
        # "has_error":False
        "form":form
    })
class ThankYouView(TemplateView):
    
    template_name="reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['message']="This works!"
        return context



# def thankyou(request):
#     return render(request,"reviews/thank_you.html")

# class ReviewsListView(TemplateView):
#     template_name= "reviews/review_list.html"
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         reviews=Review.objects.all()
#         context["reviews"]=reviews  # sends reviews to the review_list.html where it can use it in interpolation.
#         return context
class ReviewsListView(ListView):
    template_name= "reviews/review_list.html"
    model= Review
    context_object_name= "reviews"
    
    def get_queryset(self):
        base_query= super().get_queryset()
        data= base_query.filter(rating__gt=3)
        return data

     

# class SigleReviewView(TemplateView):
#     template_name= "reviews/single_review.html"
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review=Review.objects.get(pk=review_id)
#         context["review"]=selected_review
#         return context
class SigleReviewView(DetailView):
    template_name= "reviews/single_review.html"
    model=Review
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        loaded_review = self.object
        request=self.request
        favorite_id=request.session.get("favorite_review")
        context["is_favorite"]=favorite_id == str(loaded_review.id)
        return context
class AddFavoriteView(View):
    def post(self,request):
        review_id= request.POST["review_id"]
        fav_review = Review.objects.get(pk=review_id)
        # never store objects in session. Dont store complex values in session. Store simple values.
        # like strings,numbers,booleans,dictionaries
        # request.session["favorite_review"] = fav_review
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/"+review_id)
