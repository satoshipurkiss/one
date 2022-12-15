#Advent of Code Day 2
#Rock Paper Scissor Strategy Guide

import pandas as pd
import numpy as np

df = pd.read_excel('StratGuide.xlsx')

df = df.values
arr = df[:,0]
ElfN = len(arr)
Elves = np.zeros(ElfN)
n = 0

# create loop that loops round all rows in input file 
while n < ElfN:
    StratGuideL = list(arr[n])
    
    # lose scenario
    if StratGuideL[2] == 'X':
        Elves[n] += 0 # losing nets 0 points

        if StratGuideL[0] == 'A': # opponent throws rock
            Elves[n] += 3 # to lose need to throw scissors
        elif StratGuideL[0] == 'B': # opponent throws paper
            Elves[n] += 1 # to lose need to throw rock
        elif StratGuideL[0] == 'C': # opponent throws scissors
            Elves[n] += 2 # to lose need to throw paper
    
    # draw scenario
    elif StratGuideL[2] == 'Y':
        Elves[n] += 3

        if StratGuideL[0] == 'A': # opponent throws rock
            Elves[n] += 1 # to draw need to throw rock
        elif StratGuideL[0] == 'B': # opponent throws paper
            Elves[n] += 2 # to draw need to throw paper
        elif StratGuideL[0] == 'C': # opponent throws scissors
            Elves[n] += 3 # to draw need to throw scissors

    # win scenario
    elif StratGuideL[2] == 'Z':
        Elves[n] += 6

        if StratGuideL[0] == 'A': # opponent throws rock
            Elves[n] += 2 # to win need to throw paper
        elif StratGuideL[0] == 'B': # opponent throws paper
            Elves[n] += 3 # to win need to throw scissors
        elif StratGuideL[0] == 'C': # opponent throws scissors
            Elves[n] += 1 # to win need to throw rock
    
    #print(StratGuideL)
    #print(Elves[n])
    n += 1

Total = sum(Elves)

print(Total)
