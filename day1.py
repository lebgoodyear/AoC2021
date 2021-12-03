#!/usr/bin/env python3

__author__ = 'Luke Goodyear (lebgoodyear@protonmail.com)'
__date__ = 'Dec 2021'

# imports
from numpy import loadtxt

# load the data
lines = loadtxt("/Users/Luke/Documents/aoc2021.txt", comments="#", delimiter=",", unpack=False)

# count the number of data points larger than the previous data point
count = 0
for depth in range(0,len(lines)-1):
    if lines[depth+1] > lines[depth]:
        count = count+1
print(count)

# count the number of 3 consecutive data points sum larger than the sum of the previous 3 data points
count3 = 0
sum2 = lines[0] + lines[1] +lines[2]
for depth in range(1,len(lines)-2):
    sum1 = sum2
    sum2 = lines[depth] + lines[depth+1] + lines[depth+2]
    if sum2 > sum1:
        count3 = count3+1
print(count3)
