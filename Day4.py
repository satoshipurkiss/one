#Advent of Code Day 4
# Camp Cleanup

import pandas as pd
import numpy as np

df = pd.read_excel('Sections.xlsx')

df = df.values
arr = df[:,0]
ElfN = len(arr)
Elves = np.zeros(ElfN)
n = 0
overlaps = 0
# create loop that loops round all rows in input file 
while n < ElfN:
    # splitting string into list and the list into two compartments
    Sections = list(arr[n])
    #print(list(Sections))

    s = 4,3
    ranges = np.zeros(s)-1
    c = 0
    d = 0
    for i in Sections:
        try:
            i = int(i)
        except:
            i = i

        if isinstance(i,int) == False:
            c += 1
            d = 0
        else:
            ranges[c,d] = i
            d += 1 

    for i in ranges:
        if i[1] < 0:
            i[2] = i[0]
                
        else:
            i[2] = i[0]*10 + i[1]

    print(Sections)
    print(ranges)
    #part 1 solution: 
    '''
    if ranges[0,2] >= ranges[2,2] and ranges[1,2] <= ranges[3,2]:
        print('yes')
        overlaps += 1
    elif ranges[0,2] <= ranges[2,2] and ranges[1,2] >= ranges[3,2]:
        print('yes2')
        overlaps += 1
    else:
        print('no')
    '''
    #part 2 solution:
    if ranges[0,2] >= ranges[2,2] and ranges[1,2] <= ranges[3,2] or ranges[0,2] <= ranges[2,2] and ranges[1,2] >= ranges[3,2]:
        print('yes')
        overlaps += 1
    #elif 
        #print('yes2')
        #overlaps += 1
    else:
        print('no')
    n += 1 # increase the count

print(overlaps)