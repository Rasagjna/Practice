import one
print("top level in two.py")
one.myfunc()

if __name__ == "__main__":  # does this in the background
    print("two.py is being run directly")
else:
    print('two.py has been imported!')
