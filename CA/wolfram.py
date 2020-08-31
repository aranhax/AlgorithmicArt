#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sep  2018

Initially based on:
https://en.wikipedia.org/wiki/A_New_Kind_of_Science
https://github.com/brahmcapoor/cellular-automata
https://github.com/zmwangx/rule30/blob/master/rule30/automaton.py
https://faingezicht.com/articles/2017/01/23/wolfram/
https://stackoverflow.com/questions/12062920/how-do-i-create-an-image-in-pil-using-a-list-of-rgb-tuples
http://stackoverflow.com/a/10032271/562769

"""
import itertools as it
import numpy as np
from visualization import write_image

def space_states(generations, total_cells=None, initial_state='mid'):
    """

    Parameters
    ----------
    generations : int
        number of generations.
    total_cells : int, optional
        total number of cells. The default is None.
    initial_state : string, optional
        DESCRIPTION. The default is 'mid'.

    Returns
    -------
    spacetime : matrix
        matrix with the generated space state.

    """
    if total_cells is None:
        total_cells = (generations * 2) + 1

    if initial_state == 'rand':
        actual_row = np.random.randint(0, 2, size=(1, total_cells))
    else:
        actual_row = np.zeros(shape=(1, total_cells), dtype=int)
        actual_row[0, total_cells // 2] = 1

    spacetime = np.zeros(shape=(generations, total_cells), dtype=int)
    spacetime[0] = actual_row

    return spacetime

def define_rule(rulenumber):
    """
    Define the rules to be used.

    Parameters
    ----------
    rulenumber : int
        https://mathworld.wolfram.com/ElementaryCellularAutomaton.html.

    Returns
    -------
    all_rules : dictionary
        with all rules.

    """
    temprule = bin(rulenumber)[2:].zfill(8)[::-1]
    all_rules = {}
    for a, b in enumerate(it.product([0, 1], repeat=3)):
        all_rules[b] = int(temprule[a])

    return all_rules


def run_cellular_automata(image, rule_number, generations, path):
    rules = define_rule(rule_number)
    state_matrix = space_states(generations)
    n_cells = state_matrix.shape[1]

    for j, generation in enumerate(state_matrix[:-1, :]):
        # #if t//100:
        write_image(image, path, j)

        new_generation = [rules[tuple([generation[len(generation) - 1],
                                       generation[0], generation[1]])]]
        _ = [new_generation.append(rules[tuple([generation[i - 1], generation[i], generation[i + 1]])]) for i in range(1, n_cells-1)]
        new_generation.append(rules[tuple([generation[len(generation) - 2],
                                           generation[len(generation) - 1], generation[0]])])
        state_matrix[j+1, :] = new_generation
        image[state_matrix == 1] = [255, 255, 255]
