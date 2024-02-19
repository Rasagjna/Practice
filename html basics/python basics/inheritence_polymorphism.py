# # inheritance is basically  a way to form new classes using classes that have already been defined.
# class Animal():
#     def __init__(self):
#         print("Animal created")
#     def who_am_i(self,variable):

#         print("Iam an animal")

#     def eat(self):
#         print("iam eating")
# my_animal=Animal()
# my_animal
# my_animal.eat()
# my_animal.who_am_i()
# class Dog(Animal):
#     def __init__(self):
#         print("this is inside dog class")
#         Animal.__init__(self)
#
#         print("dog created")
#     def who_am_i(self):
#         print("Iam a dog")
#     def eat(self):
#         print("iam dog and eating")
#
#     def bark(self):
#         print("WOOF")
# mydog=Dog()
# mydog.eat()
# mydog.bark()
# mydog.who_am_i() # method overriding

# //////////////////////////////////////////////////////
# POLYMORPHISM- DIFFERENT  OBJECT CLASSES SHARE THE SAME METHOD NAME. Two different classes sharing the same method name!
# class Dog():
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return self.name + " says woof!"
#
#
# class Cat():
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return self.name + " says meow!"
#
#
# niko = Dog("niko")
# felix = Cat("felix")
# print(niko.speak())
# print(felix.speak())
#
# for pet in [niko, felix]:
#     print(type(pet))
#     print(type(pet.speak()))
#
#
# # both niko and felix share the same method name called speaks but are of different types
# def pet_speak(pet):
#     print(pet.speak())
#
#
# pet_speak(niko)
# pet_speak(felix)
#
# class Animal():
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this abstract method")
# myanimal=Animal('feed')
# # myanimal.speak() #error. Base class doesnot do anything. just defines structure
#
# class Dog(Animal):
#     def speak(self):
#         return self.name + " says woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return self.name + " says meow!"
# fido=Dog("Fido")
# isis=Cat("Isis")
# print(fido.speak())
# print(isis.speak())
# #/////////////////////////////////////////
# mylist=[1,2,3]
# print(len(mylist))
# class Book():
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#     def __len__(self):
#         return self.pages
#     def __del__(self):
#         print("a book obj has been deleted")
#
# b=Book('pyhton rocks','jose',200)
# print(b)
# print(str(b))
# print(len(b))
# del b
# print(b)
# class Parent1:  # parent class 1
#     variable = "hi"
#
#     def foo(self):
#         print('called Parent1-foo()')
#
#
# class Parent2:  # parent class 2
#     def foo(self):
#         print('called Parent2-foo()')
#
#     def bar(self):
#         print('called Parent2-bar()')
#
#
# class Child1(Parent1, Parent2):  # child 1 derived from Parent1, Parent2
#     pass
#
#
# class Child2(Parent1, Parent2):
#     # child 2 derived from Parent1, Parent2
#     def __init__(self):
#         super().__init__()
#         # Parent1.__init__(self)
#
#
#     def foo(self):  # over riding methods
#         print('called Child2-foo()')
#
#     def bar(self):
#         print('called Child2-bar()')

#
# class GrandChild(Child1, Child2):  # define grandchild class
#     pass  # derived from Child1 and Child
#
#
# gc = GrandChild()
# gc.foo()  # called Child2-foo()
# gc.bar()  # called Child2-bar()
# Parent1.foo(gc)
class A():
    def __init__(self):
        print("this is super class A")
class B():
    def __init__(self):
        print("this is super class B ")
class C(A,B):
    super().__init__()
c=C()
c

