#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 12:51:01 2018

Initially based on:
https://en.wikipedia.org/wiki/A_New_Kind_of_Science
https://github.com/brahmcapoor/cellular-automata
https://github.com/zmwangx/rule30/blob/master/rule30/automaton.py
https://faingezicht.com/articles/2017/01/23/wolfram/

@author: aranildo
"""


import numpy as np
import itertools as it

def states(n_generations=100, n_cells=None, initial_state = 'mid'):
    if n_cells is None:
        n_cells = (n_generations *2) +1
    
    if initial_state == 'rand':
        actual_row = np.random.randint(0, 2, size=(1, n_cells))
    else:
        actual_row = np.zeros(shape=(1, n_cells),dtype=int)
        actual_row[0,n_cells //2] = 1
    
    spacetime = np.zeros(shape=(n_generations, n_cells),dtype=int)
    spacetime[0] = actual_row

    return spacetime
    
def define_rule(rulenumer):
    temprule =  bin(rulenumer)[2:].zfill(8)[::-1]
    
    all_rules = {}    
    for a,b in enumerate(it.product([0,1], repeat=3)):
        all_rules[b] =  int(temprule[a])
    
    return all_rules    

ca_rules = define_rule(150)
ss = states(45)    
n_cells = ss.shape[1]

print(''.join(map(str, ss[0,:]))) 
for j,generation in enumerate(ss[:-1,:]):
    new_generation = [ca_rules[tuple([generation[len(generation) - 1], generation[0], generation[1]])]]
    _  =   [new_generation.append(ca_rules[tuple([generation[i - 1], generation[i], generation[i + 1]])]) for i in range(1,n_cells-1)]
    new_generation.append(ca_rules[tuple([generation[len(generation) - 2], generation[len(generation) - 1], generation[0]])])
    print(''.join(map(str, new_generation))) 
    ss[j+1,:] = new_generation

