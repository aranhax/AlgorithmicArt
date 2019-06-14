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
from statistics import mode

def states(n_generations=50, size=(10,10)):    
    actual_row = np.random.randint(0, 3, size=size)    
    spacetime = np.zeros(size + (n_generations,),dtype=np.int8)
    spacetime[:,:,0] = actual_row

    return spacetime


def define_rule(element,size, time):
    
    if element[0] == size[0]-1:
        vote = mode([spacetime[element[0]-1,element[1],time], spacetime[element[0],element[1]-1,time], spacetime[element[0],element[1]+1,time],  spacetime[0,element[1],time]])
    elif element[1] == size[1]-1:
        vote = mode([spacetime[element[0]-1,element[1],time], spacetime[element[0],element[1]-1,time], spacetime[element[0],0,time], spacetime[element[0]+1,element[1],time]])
    elif (element[0] == size[0]-1) and (element[1] == size[1]-1):
        vote = mode([spacetime[element[0]-1,element[1],time], spacetime[element[0],element[1]-1,time], spacetime[element[0],0,time], spacetime[0,element[1],time]])
    else:
        vote = mode([spacetime[element[0]-1,element[1],time], spacetime[element[0],element[1]-1,time], spacetime[element[0],element[1]+1,time], spacetime[element[0]+1,element[1],time]])
        
    return vote





n_generations=100
rule = 150

ca_rules = define_rule(rule)

ss = states(n_generations)


n_cells = ss.shape[1]

save_path_figures = "/home/aranildo/temp/art/gif/test/"

import numpy as np
import scipy.misc as smp

# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros( (1024,1024,3), dtype=np.uint8 )

data[512,512] = [0,255,0]       # Makes the middle pixel red
data[512,513] = [0,0,255]       # Makes the next pixel blue

img = smp.toimage( data )       # Create a PIL image
img.show()      


# Image size
width = n_cells
height = n_generations
#channels = 1
channels = 3
# Create an empty image
img = np.zeros((10, 10, channels), dtype=np.uint8)

img[0][:] = np.repeat(np.expand_dims(ss[0,:,0] * 255, axis=1) , 3, axis=1)

for j,generation in enumerate(ss[:-1,:]):
    #plt.rcParams["figure.figsize"] = (width,height)
    #plt.rcParams["figure.dpi"] = 100
    plt.rcParams["savefig.transparent"]=True
    plt.rcParams["savefig.bbox"]='tight'
    plt.rcParams["savefig.edgecolor"] = 'black'
    plt.rcParams["savefig.facecolor"] = 'black'

    new_generation = [ca_rules[tuple([generation[len(generation) - 1], generation[0], generation[1]])]]
    _  =   [new_generation.append(ca_rules[tuple([generation[i - 1], generation[i], generation[i + 1]])]) for i in range(1,n_cells-1)]
    new_generation.append(ca_rules[tuple([generation[len(generation) - 2], generation[len(generation) - 1], generation[0]])])    
    img[j][:] = np.repeat(np.expand_dims([x * 255 for x in new_generation] , axis=1), 3, axis=1)
    ss[j+1,:] = new_generation
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(save_path_figures + 'Frame' + str(j+1).zfill(3) + '.jpeg', format='jpeg')
    plt.close('all')
