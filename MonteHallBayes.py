#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
 
# N Samples
N = 10000
 
#Define an array of the different doors with the car at random
cars = np.random.randint(0,high=3,size=N)+1
#define an array of the different doors, and picks at random
picks = np.random.randint(0,high=3,size=N)+1
 
#Counters for win if stay and switch
count_stay =0
count_switch =0
 
 
for i in range(N):
    #define array of 3 doors
    doors_round1 = [1,2,3]
 
    #First we have to remove both the car and the pick
    doors_round1.remove(picks[i])
    if cars[i] != picks[i]:
        doors_round1.remove(cars[i])
 
    #Will open one door at random.
    #If Cars and Picks are the same door, it can only choose one.
    open_door = doors_round1[np.random.randint(len(doors_round1))]
 
    doors_round2 = [1,2,3]
    doors_round2.remove(open_door)
 
    #Switch picks
    doors_round2.remove(picks[i])
    pick2 = doors_round2[0]
 
 
    if  cars[i] == picks[i]:
        count_stay = count_stay + 1
 
    if  cars[i] == pick2:
        count_switch = count_switch + 1
 
print("\nStay: %d"%(100*count_stay/N))
print("Switch: %d"%(100*count_switch/N))

