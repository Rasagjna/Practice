# from django.shortcuts import render,get_object_or_404
# from .models import Book
# from django.http import Http404
# from django.db.models import Avg
# # Create your views here.
# def index(request):
#     books=Book.objects.all().order_by("-title")# - before title indicates order by descending order
#     num_books=books.count()
#     avg_rating=books.aggregate(Avg("rating")) # rating__avg
#     return render(request,"book_outlet/index.html",{
#         "books":books,
#         "total_no_of_books":num_books,
#         "average_rating":avg_rating
#     })
# # def book_details(request,id): # replace id by slug
# def book_details(request,slug):
#     try:
#         # book=Book.objects.get(pk=id)
#         book=Book.objects.get(slug=slug)

#     except:
#         raise Http404()
#     # book=get_object_or_404(Book,pk=id)

#     return render(request,"book_outlet/book_detail.html",{
#         "title":book.title,
#         "author":book.author,
#         "rating":book.rating,
#         "is_bestseller":book.is_bestselling
#     })

