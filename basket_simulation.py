#  -*- coding: utf-8 -*-
'''
P5
Derek Nguyen
Created: 2019-03-06
Modified: 2019-03-06
Due: 2019-03-06
'''

# %% codecell

import numpy as np
import matplotlib # used to create interactive plots in the Hydrogen package of the Atom IDE
matplotlib.use('Qt5Agg') # used to create interactive plots in the Hydrogen package of the Atom IDE
import matplotlib.pyplot as plt

def Shot_Probability(information = 'a'):
    '''
    Calculating the probability of making the 100th shot given that the probability of making each shot is the fraction of shots/total number of shots
    Parameters:
    information, can be 'a', 'b', or 'c' which represent the conditions specified in p5
    '''

    shots = 1 # sets initial statistics
    total = 2

    if information == 'a': # sets information a from p5 prompt which was no additional information
        for shot in np.arange(100):
            if np.random.uniform() < shots/total: # add 1 count to shots if the shot is made
                shots += 1

            total += 1

    if information == 'b': # sets information b from p5 prompt which was making the 99th shot
        for shot in np.arange(100):
            if shot == 98: # 99th shot is a guarnteed to be made
                shots += 1
            elif np.random.uniform() < shots/total: # add 1 count to shots if the shot is made
                shots += 1

            total += 1

    if information == 'c': # sets information c from p5 prompt which was 53:56 and 99 shots were made while 57 was a miss
        for shot in np.arange(100):
            if shot == 52: # shots 53:56 guarnteed successes
                shots += 1
            elif shot == 53: # shots 53:56 guarnteed successes
                shots += 1
            elif shot == 54: # shots 53:56 guarnteed successes
                shots += 1
            elif shot == 55: # shots 53:56 guarnteed successes
                shots += 1
            elif shot == 98: # shot 98 guarnteed successes
                shots += 1

            elif shot == 56: # 57th shot is a miss
                shots += 0
            elif np.random.uniform() < shots/total: # add 1 count to shots if the shot is made
                shots += 1

            total += 1

    return shots/total

def Shot_Simulation(numTrials = 10000, information = 'a'):
    '''
    Simulates the probability of making the 100th shot utilizing n number of trials given that the probability of making each shot is the fraction of shots/total number of shots.
    Utilizes function Shot_Probability.
    Parameters:
    numTrials, a number of trials to be performed
    information, can be 'a', 'b', or 'c' which represent the conditions specified in p5
    '''
    x = np.zeros(numTrials) # preallocate data set

    for trial in np.arange(numTrials): # iterate through numTrials
        x[trial] = Shot_Probability(information)

    avg = np.average(x) # calculate avg probability

    print('The probability of making the 100th shot with conditions {} is {}'.format(information, avg))

Shot_Simulation(information = 'c')
