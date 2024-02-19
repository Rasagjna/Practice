# from collections import Counter
#
# mylist = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
# print(Counter(mylist))
# print(Counter('aaaabbbbbhbhahaa'))
# sentence = "how many times does each word show up in this sentence with a word"
# print(Counter(sentence.split()))
# letters = "aaabbbbbbcccccccddddddd"
# c = Counter(letters)
# print(c)
# print(c.most_common(2))  # 2 most common
# print(c.items())
# print(list(c))
# # /////////// default dictionary////////////
#
# from collections import defaultdict
#
# d = {'a': 10}
# print(d['a'])
# d = defaultdict(lambda: 0)
# d['correct'] = 100
# print(d['wrong'])  # assigns default value of 0 rather than raising an error
# print(d)
#
# # ///////////// named tuple//////////////////
# mytuple = (10, 20, 30)
# print(mytuple[0])
# from collections import namedtuple
#
# Dog = namedtuple('Dog', ['age', 'breed', 'name'])
# sammy = Dog(age=5, breed="Husky", name="Sam")
# print(type(sammy))
# print(sammy.age, sammy.breed, sammy.name)

# ///////////////////////////
f = open('practice.txt', 'w+')
f.write('this is a test string')
f.close()
import os

print(os.getcwd())
print(os.listdir())
print(os.listdir('C:\\Users'))

import shutil
# shutil.move('practice.txt',<dest>)
import send2trash

send2trash.send2trash('practice.txt')
print(os.listdir())
file_path = 'D:\\html basics\\python basics\\simple1.py'
for folder, sub_folders, files in os.walk(file_path):
    print(f"currently looking at {folder}")
    print('\n')
    print('the subfolders are')
    for sub_fold in sub_folders:
        print(f"Subfolder:{sub_fold}")
    print('\n')
    print("the files are:")
    for f in files:
        print(f"\tFile:{f}")
    print('\n')
