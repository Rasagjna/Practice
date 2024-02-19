#
#
#
# def myfunc():
#     print("myfunc()")
#
#
# if __name__ == "__main__":  # does this in the background
#     print("one.py is being run directly")
# else:
#     print('one.py has been imported!')
# try:
#     for i in ['a', 'b', 'c']:
#         print(i ** 2)
# except TypeError:
#     print("error")
while True:
    try:
        n = int(input())
    except:
        print("error")
        continue
    else:
        break
    finally:
        print("finally block")
print(n ** 2)
