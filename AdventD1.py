#Advent of Code Day 1
#Calorie counting

import pandas as pd
import numpy as np
import math

df = pd.read_excel('Elf Calories.xlsx')
df = df.values
arr = df[:,0]
ElfN = len(arr)
Elves = np.zeros(ElfN)

n = 0 
m = 0

# create loop that loops round all rows in input file 
while n < ElfN:
    if math.isnan(arr[n])== False:
        Elves[m] = Elves[m]+(arr[n])
    else:
        m +=1
    n += 1

#Q1 part 1 Solution:
print (max(Elves))

#Q1 part 2 solution:
Elves_sorted = sorted(Elves, reverse = True)
top3 = sum(Elves_sorted[0:3])

print(top3)
