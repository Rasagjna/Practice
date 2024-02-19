# # def create_cubes(n): # need to create an entire list of numbers and iterate over them
# #     result=[]
# #     for x in range(n):
# #         result.append(x**3)
# #     return result
# # print(create_cubes(10))
# def create_cubes(n):
#     for x in range(n):
#         yield x**3
# print(create_cubes(10)) # more efficient.Not stored in memory
# list(create_cubes(10))
# # for x in create_cubes(10):
# #     print(x)
# def gen_fib(n):
#     a=1
#     b=1
#     op=[] # less memory efficient. therefore always use yield.
#     for i in range(n):
#         yield a
#         # op.append(a)
#         a,b=b,a+b
#     # return op
# for num in gen_fib(10):
#     print(num)
#
# def simple_gen():
#     for x in range(3):
#         yield x
# for num in simple_gen():
#     print(num)
# g=simple_gen()
# print(g)
# print(next(g))
# print(next(g))
# #/////////////////////////
# s="hello"
# for l in s:
#     print(l)
# s_iter = iter(s)
# print(next(s_iter))
# print(next(s_iter))

# HOME WORK
import random


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)
for n in rand_num(1,10,12):
    print(n)
print(rand_num(1,10,13))

 #2
s="hello"
s_iter=iter(s)
print(s_iter)
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)
print(gencomp)
for item in gencomp:
    print(item)