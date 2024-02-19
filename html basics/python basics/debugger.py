import pdb

x = [1, 2, 3, 4]
y = 2
z = 3
result1 = y + z
# setting trace before error line. provides interactive environment to know wha
pdb.set_trace()
result2 = x + y
