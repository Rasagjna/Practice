from datetime import date

from django.shortcuts import render

all_posts=[
    {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Maximilian",
        "date":date(2021,7,10),
        "excerpt":"Theres nothing like the views you get when hiking in the mountains!And I wasnt even prepared for what happened whilst I was enjoying the view!",
         "content":"""
         kfjhfbjabgerbgijgh  nsjkbgerib
         sjkghrjbgehj gfd nbjdhbgiwgnab
         faesjgbrhjgbnfdk vdkjfgnwr
         """
    },
     {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Maximilian",
        "date":date(2021,7,9),
        "excerpt":"Theres nothing like the views you get when hiking in the mountains!And I wasnt even prepared for what happened whilst I was enjoying the view!",
         "content":"""
         kfjhfbjabgerbgijgh  nsjkbgerib
         sjkghrjbgehj gfd nbjdhbgiwgnab
         faesjgbrhjgbnfdk vdkjfgnwr
         """
    },
     {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Maximilian",
        "date":date(2021,7,9),
        "excerpt":"Theres nothing like the views you get when hiking in the mountains!And I wasnt even prepared for what happened whilst I was enjoying the view!",
         "content":"""
         kfjhfbjabgerbgijgh  nsjkbgerib
         sjkghrjbgehj gfd nbjdhbgiwgnab
         faesjgbrhjgbnfdk vdkjfgnwr
         """
    }
]
# Create your views here.

def get_date(post):
    return post['date']
def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",
    {
        "posts":latest_posts
    })

def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts
    })
def post_detail(request,slug):
    identified_post=next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blog/posts-detail.html",{
      "post":identified_post  
    }
    
    )
    