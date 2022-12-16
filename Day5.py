#Advent of Code Day 4
# Camp Cleanup
import pandas as pd
import numpy as np

from request_input_data import get_input
data = get_input(4)

df = pd.read_excel('Sections.xlsx')

df = df.values
arr = df[:,0]
ElfN = len(arr)
Elves = np.zeros(ElfN)
n = 0


# create loop that loops round all rows in input file 
while n < ElfN:
    # splitting string into list and the list into two compartments
    Sections = list(arr[n])

    n += 1 # increase the count


##################