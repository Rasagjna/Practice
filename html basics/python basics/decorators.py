# def func():
#     return 1
# def hello(name="jose"):
#     print("the hello func has been executed")
#     # return "hello"
#     def greet():
#         return '\t this is the greet() func inside hello!'
#     # print(greet())
#     def welcome():
#         return '\t this is welcome() inside hello'
#     # print(welcome())
#     # print("this is the end of the hello func!")
#     print("iam going to return a func")
#     if name=="jose":
#         return greet
#     else:
#         return welcome
# # hello()
# greet=hello
# print(greet())
# del hello
# print(greet())
# --------------- assigning variable to a function------------------
# my_new_func=hello('jose')
# print(my_new_func())
# def cool():
#     def super_cool():
#         return "iam very cool"
#     return super_cool
# some_func=cool()
# print(some_func())


# //////////////////passing func as an argument////////////
# def hello():
#     return "hi jose"
# def other(some_def_func):
#     print("other code runs here!")
#     print(some_def_func())
# other(hello)
#


# //////////////decorators/////////////////
def new_decorator(original_func):
    def wrap_func():
        print("some extra code, before the original func")
        original_func()
        print("some extra code after original func")

    return wrap_func


def func_needs_decorator():
    print("i want to be decorated!!")


decorated_func = new_decorator(func_needs_decorator)
decorated_func()

# ------------@ operator-----------
print("using @ operator")


@new_decorator
def func_needs_decorator():
    print("i want to be decorated!!")
func_needs_decorator()


@new_decorator
def hello():
    print("hello")


hello()
