#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 12:51:01 2018

Initially based on:
https://en.wikipedia.org/wiki/A_New_Kind_of_Science
https://github.com/brahmcapoor/cellular-automata
https://github.com/zmwangx/rule30/blob/master/rule30/automaton.py
https://faingezicht.com/articles/2017/01/23/wolfram/
https://stackoverflow.com/questions/12062920/how-do-i-create-an-image-in-pil-using-a-list-of-rgb-tuples
http://stackoverflow.com/a/10032271/562769

@author: aranildo
"""

import numpy as np
import itertools as it
import matplotlib.pyplot as plt
import scipy.misc as smp

def states(n_generations=50, size=(10,10)):    
    actual_row = np.random.randint(0, 3, size=size)    
    #spacetime = np.zeros(size + (n_generations,),dtype=np.int8)
    spacetime = np.zeros(size ,dtype=np.int8)
    spacetime[:,:] = actual_row

    return spacetime


def define_rule(element,size, time):
    
    if element[0] == size[0]-1:
        vote = find_majority([spacetime[element[0]-1,element[1],time], spacetime[element[0],element[1]-1,time], spacetime[element[0],element[1]+1,time],  spacetime[0,element[1],time]])
    elif element[1] == size[1]-1:
        vote = find_majority([spacetime[element[0]-1,element[1],time], spacetime[element[0],element[1]-1,time], spacetime[element[0],0,time], spacetime[element[0]+1,element[1],time]])
    elif (element[0] == size[0]-1) and (element[1] == size[1]-1):
        vote = find_majority([spacetime[element[0]-1,element[1],time], spacetime[element[0],element[1]-1,time], spacetime[element[0],0,time], spacetime[0,element[1],time]])
    else:
        vote = find_majority([spacetime[element[0]-1,element[1],time], spacetime[element[0],element[1]-1,time], spacetime[element[0],element[1]+1,time], spacetime[element[0]+1,element[1],time]])
        
    return vote

def define_rule_notime(spacetime, element):    
    size = spacetime.shape
    if (element[0] == size[0]-1) and (element[1] == size[1]-1):
        vote = find_majority([spacetime[element[0]-1,element[1]], spacetime[element[0],element[1]-1], spacetime[element[0],0], spacetime[0,element[1]]])
    elif element[0] == size[0]-1:
        vote = find_majority([spacetime[element[0]-1,element[1]], spacetime[element[0],element[1]-1], spacetime[element[0],element[1]+1],  spacetime[0,element[1]]])
    elif element[1] == size[1]-1:
        vote = find_majority([spacetime[element[0]-1,element[1]], spacetime[element[0],element[1]-1], spacetime[element[0],0], spacetime[element[0]+1,element[1]]])
    else:
        vote = find_majority([spacetime[element[0]-1,element[1]], spacetime[element[0],element[1]-1], spacetime[element[0],element[1]+1], spacetime[element[0]+1,element[1]]])
        
    return vote

from collections import Counter

def find_majority(votes):
    vote_count = Counter(votes)
    top_two = vote_count.most_common(2)
    if len(top_two)>1 and top_two[0][1] == top_two[1][1]:
        # It is a tie
        return 0
    return top_two[0][0]


save_path_figures = "/home/aranildo/temp/art/gif/test/"


width = 1920
height = 1080

# Create a 1024x1024x3 array of 8 bit unsigned integers
data_img = np.zeros((height,width,3), dtype=np.uint8 )
ss = states(size=(height,width))
# serial
for t in range(300):
    for t2 in range(width*20):#*height):
        elem = [np.random.randint(0, height),np.random.randint(0, width)]
        ss[elem[0],elem[1]] = define_rule_notime(ss,(elem[0],elem[1]))
        
    data_img[ss == 0] = [255,0,0] 
    data_img[ss == 1] = [0,255,0] 
    data_img[ss == 2] = [0,0,255] 
    
    img = smp.toimage(data_img)       # Create a PIL image
    #if t//100: 
    img.save(save_path_figures + 'Frame' + str(t+1).zfill(3) + '.jpeg')


img.show()      


# Image size
