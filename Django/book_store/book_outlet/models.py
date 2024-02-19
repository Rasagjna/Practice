from distutils.command.build_scripts import first_line_re
import imp
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
from django.urls import reverse
from django.utils.text import slugify

class Country(models.Model):
    name= models.CharField(max_length=80)
    code= models.CharField(max_length=2)
    class Meta:
        verbose_name_plural = "Countries"
    def __str__(self):
        return self.name


class Address(models.Model):
    street=models.CharField(max_length=80)
    postal_code=models.CharField(max_length=5)
    city=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.street},{self.postal_code},{self.city}"
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address= models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title=models.CharField(max_length =50 )
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    # author=models.CharField(null=True,max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")# relating author to BOOK.
    is_bestselling= models.BooleanField(default = False)
    slug=models.SlugField(default="",blank=True,null=False,
    db_index=True)# HArry Potter 1 =>Harry-potter-1
    published_countries= models.ManyToManyField(Country,related_name="books")
    def get_absolute_url(self):
        return reverse("book_details", args=[self.slug])
        # return reverse("book_details", args=[ self.id])
    # def save(self,*args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title}({self.rating})"

