#Advent of Code Day 3
#Compartment Organisation

import pandas as pd
import numpy as np

df = pd.read_excel('Rucksacks.xlsx')

df = df.values
arr = df[:,0]
#print(arr)
ElfN = len(arr)
Elves = np.zeros(ElfN)
#print(ElfN)
n = 0

# create loop that loops round all rows in input file 
while n < ElfN:
    # splitting string into list and the list into two compartments
    Rucksack = list(arr[n:n+3])

    # used for part 1:
    '''
    RucksackSize = len(Rucksack)
    Comp1 = Rucksack[0:int(RucksackSize/2)]
    Comp2 = Rucksack[int(RucksackSize/2):RucksackSize]
    duplicate = set(Comp1).intersection(Comp2) # identifying duplicate
    '''
    # part 2 
    duplicate = set(Rucksack[0]).intersection(Rucksack[1]).intersection(Rucksack[2]) # identifying duplicate
    
    asciiNdup = ord(list(duplicate)[0]) - 96   # prioritising item by alphabet and if it is capitalised
    if asciiNdup < 1:
        asciiNdup += 32 + 26
    
    Elves[n] = asciiNdup
    
    n += 3 # increase the count

Total = sum(Elves)
print(Total)