import math

value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(4.35))
print(round(4.5))
print(round(5.5))
print(math.pi)
print(math.e)
# numpy
print(math.log(math.e))
print(math.log(100, 10))
print(math.sin(10))
print(math.degrees((math.pi) / 2))
print(math.radians(180))
import random

print(random.randint(0, 100))
random.seed(101)  # sets the proper sequence
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
mylist = list(range(0, 20))
print(random.choice(mylist))
# sample with replacement
print(random.choices(population=mylist, k=10))
#sample without replacement
print(random.sample(population=mylist,k=10))
random.shuffle(mylist)
print(mylist)
# randomly pick a value between a and b ,allows floating point
print(random.uniform(a=0,b=100))
print(random.gauss(mu=0,sigma=1))

