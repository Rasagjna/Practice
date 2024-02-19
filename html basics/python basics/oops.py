# oops allows users to create their own objects with their owm methods and attributes.
#programs become flexible
# class NameOfClass(): # camel case **
#     def __init__(self,param1,param2): # allows you to create instance of obj
#         self.param1=param1
#         self.param2=param2
#     def some_method(self):
#         print(self.param1)

l=[1,2,3]
s=set()
print(type(s))
print(type(l))
# class is a blueprint which defines nature of the future object
# from class we can instances called objects
class Dog():
    # class obj attribute. same for any instance of class
    species='mammal'
    # methods are essentially functions defined inside the body of the class.
    # functions acting on object
    def __init__(self,mybreed,name,spots): # constructor of the class
        self.breed=mybreed
        self.name=name
        self.spots=spots # expect boolean true/false.
        # breed is attribute
        # by convention all 3 have same name. But it is not necessary.
    def bark(self,num):
        print("WOOF! my name is {} and num is {}".format(self.name,num))

mydog=Dog(mybreed='Lab',name='Sammy',spots=False)
print(type(mydog))
print(mydog.breed)# mybreed is only the argument name. breed is attribute.In convention they named alike to avoid confusion.
print(mydog.spots)
print(mydog.name)
print(Dog.species)
print(mydog.species)
mydog.bark(90)


class Circle():
    # class obj attribute
    pi =3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.area= radius*radius*Circle.pi
    def get_circumference(self):
        return self.radius*self.pi*2
mycircle=Circle(30)# ovverriding default value of radius
print("circumference of circle",mycircle.get_circumference())
print("area of circle",mycircle.area)

# called upon when we create instance of class
# self keyword allows you to connect this method to instance of the class
#it allows us to refer to itself. Instance of the obj itself. similar to this in java.

# my_sample=Sample() # instance of class
# print(my_sample)