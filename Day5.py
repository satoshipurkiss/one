# Advent of Code Day 5
# Supply Stacks

import pandas as pd
import numpy as np
#from builtins import str

df = pd.read_excel('CargoPlane.xlsx')
print(df[0:8])
arr = df.values[:,0]
s = df.squeeze()
# print(s)
# s = s.str.split(']',expand = True)
# print(s)
# arr = df[:,0]
ElfN = len(df.index)
Elves = np.zeros(ElfN)
n = 0

# print(df[:,0])
planeN = 0

while planeN < 9:
    
    for i in arr:
        print('i is ',i)
        str(i)
        for j in i:
            print('j is ',j)
            plane = "test"
            spaces = 0
            if j == "[":
                plane += j
            elif j == " ":
                spaces += 1
                print(spaces)
            else:
                plane += str(j)
            print(plane)

    planeN += 1
# create loop that loops round all rows in input file 
while n < ElfN:
    # splitting string into list and the list into two compartments
    # Sections = s[n].squeeze
    # print(s)
    # s = s.str.split(' ',expand = True)
    n += 1 # increase the count
