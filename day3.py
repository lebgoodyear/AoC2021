#!/usr/bin/env python3

__author__ = 'Luke Goodyear (lebgoodyear@protonmail.com)'
__date__ = 'Dec 2021'

# imports
import numpy as np
# load the data
diagnostics = np.genfromtxt("/Users/Luke/Documents/AoC2021/day3.txt", dtype=str)

# define function to split string into individual characters
def split(word):
        return [char for char in word]

# split values into individual units for column comparisons
for report in range(0, len(diagnostics)):
    d = np.array(split(diagnostics[report]))
    if report == 0:
        d_split = d
    elif report == 1:
        d_split = np.stack((d_split, d), axis=0)
    else:
        d_split = np.insert(d_split, report, d, axis=0)

# change to data type integer
d_split = d_split.astype('object')
d_split[:,:] = d_split[:,:].astype(np.int)


############################# Part 1 ##################################


# count occurrences of 0s and 1s in each column respectively
count0_array = np.count_nonzero(d_split == 0, axis=0)
count1_array = np.count_nonzero(d_split == 1, axis=0)

# choose most commonly occurring variable (1 or 0) and store in 1d array
gamma = []
for parameter in range(0, len(count0_array)):
    if count0_array[parameter] > count1_array[parameter]:
        gamma.append(0)
    else:
        gamma.append(1)

# choose least commonly occurring variable (1 or 0) and store in 1d array
epsilon = np.repeat(0, 12)
for i in range(0,len(gamma)):
    if gamma[i] == 0:
        epsilon[i] = 1

# convert to list
epsilon = epsilon.tolist()

# recombine characters in order to use whole binary number
gamma_str = "".join(str(i) for i in gamma)
epsilon_str = "".join(str(i) for i in epsilon)
    
# convert to decimal and multiply
total_ge = np.int(gamma_str,2) * np.int(epsilon_str,2)


############################# Part 2 ##################################


# loop over parameters and discard any records with least common value at parameter value
ox = d_split
for parameter in range(0, np.shape(d_split)[1]):
    # count occurrences of 0s and 1s in each column respectively
    count0_array = np.count_nonzero(ox == 0, axis=0)
    count1_array = np.count_nonzero(ox == 1, axis=0)
    # find most common value at parameter
    if count0_array[parameter] > count1_array[parameter]:
        gamma = 0
    else:
        gamma = 1
    # count number of records to loop over
    top = np.shape(ox)[0]
    to_del = []
    # as soon as only one record remains, stop
    if top > 1:
        # remove any records not equal to most common parameter value
        for record in range(0, top):
            if ox[record, parameter] != gamma:
                to_del.append(record)
        ox = np.delete(ox, to_del, axis=0)

# loop over parameters and discard any records with most common value at parameter value
co2 = d_split
for parameter in range(0, np.shape(d_split)[1]):
    # count occurrences of 0s and 1s in each column respectively
    count0_array = np.count_nonzero(co2 == 0, axis=0)
    count1_array = np.count_nonzero(co2 == 1, axis=0)
    # find most least value at parameter
    if count0_array[parameter] > count1_array[parameter]:
        gamma = 0
    else:
        gamma = 1
    # count number of records to loop over
    top = np.shape(co2)[0]
    to_del = []
    # as soon as only one record remains, stop
    if top > 1:
        # remove any records not equal to most common parameter value
        for record in range(0, top):
            if co2[record, parameter] == gamma:
                to_del.append(record)
        co2 = np.delete(co2, to_del, axis=0)

# convert to lists
ox = ox.tolist()
co2 = co2.tolist()

# recombine characters in order to use whole binary number
ox_str = "".join(str(i) for i in ox[0])
co2_str = "".join(str(i) for i in co2[0])
    
# convert to decimal and multiply
lsr = np.int(ox_str,2) * np.int(co2_str,2)


## end of script