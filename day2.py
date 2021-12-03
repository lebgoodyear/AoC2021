#!/usr/bin/env python3

__author__ = 'Luke Goodyear (lebgoodyear@protonmail.com)'
__date__ = 'Dec 2021'

# imports
import numpy as np
# load the data
lines = np.genfromtxt("/Users/Luke/Documents/AoC2021/day2.txt", dtype=str)

# convert data type to object and then to float to enable maths operators
lines = lines.astype('object')
lines[:,1] = lines[:,1].astype(np.float)

# for loop to count movements forward and down
forward = 0
depth = 0
for instr in range(0,len(lines)):
    if lines[instr,0] == 'forward':
        forward = forward + lines[instr,1]
    elif lines[instr,0] == 'up':
        depth = depth - lines[instr,1]
    else:
        depth = depth + lines[instr,1]

total = depth*forward

# for loop to convert movements forward and down for new instructions
forward = 0
depth = 0
aim = 0
for instr in range(0,len(lines)):
    if lines[instr,0] == 'forward':
        forward = forward + lines[instr,1]
        depth = depth + aim * lines[instr,1]
    elif lines[instr,0] == 'up':
        aim = aim - lines[instr,1]
    else:
        aim = aim + lines[instr,1]

total = depth*forward

