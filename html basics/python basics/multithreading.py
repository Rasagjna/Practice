import threading
from threading import *
from time import *
import concurrent.futures


#
# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)
#
#
# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")
#             sleep(1)
#
#
# t1 = Hello()
# t2 = Hi()
# t1.start()
# sleep(0.2)
# t2.start()
# t1.join()
# t2.join()
# main thread - t1- hello,t2-hi
# two threads going to the cpu at the same time. COllision
# 3 threads- main thread, t1,t2
# print("bye")
# main thread prints bye.
# /////////////////////////////////////////////
#
# def calc_square(numbers):
#     print("calculate square of numbers")
#     for n in numbers:
#         print(n ** 2, "square")
#         sleep(0.2)
#
#
# def cal_cube(numbers):
#     print("calculate cube of numbers")
#     for n in numbers:
#         print(n ** 3, "cube")
#         sleep(0.2)
#
#
# arr = [2, 3, 4, 5]
# t = time()
# t1 = threading.Thread(target=calc_square, args=(arr,))
# t2 = threading.Thread(target=cal_cube, args=(arr,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# # calc_square(arr)
# # cal_cube(arr)
# print("done in", time() - t)


def do_something(seconds):
    print(f"hi , sleeping{seconds}")
    sleep(seconds)
    return f'done sleeping{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something)
    # f2 = executor.submit(do_something)
    secs=[5,4,3,2,1]
    # results=[executor.submit(do_something,sec) for sec in secs]
    # # print(f1.result())
    # # print(f2.result())
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    results=executor.map(do_something,secs)
    for result in results:
        print(result)


#
# threads = []
# ti = time()
# for i in range(10):
#     t = threading.Thread(target=do_something)  # creating multiple threads
#     t.start()
#     threads.append(t)
# for thread in threads:
#     thread.join()
#
# print("done in", time() - ti)
