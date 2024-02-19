
from django.urls import path

from . import views

urlpatterns=[
    # path("",views.review),
 path("",views.ReviewView.as_view())   ,
# path("thank-you",views.thankyou)
path("thank-you",views.ThankYouView.as_view()),
path("reviews",views.ReviewsListView.as_view()),
path("reviews/favorite",views.AddFavoriteView.as_view()),
# path("reviews/<int:id>",views.SigleReviewView.as_view()),
path("reviews/<int:pk>",views.SigleReviewView.as_view())
]