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
from os.path import join
import numpy as np
import itertools as it
from PIL import Image

def space_states(generations, total_cells=None, initial_state='mid'):

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

def define_rule(rulenumer):
    temprule = bin(rulenumer)[2:].zfill(8)[::-1]
    all_rules = {}
    for a, b in enumerate(it.product([0, 1], repeat=3)):
        all_rules[b] = int(temprule[a])

    return all_rules

def create_initial_image(img_height, img_width, img_channels,
                         background_color=None):

    initial_img = np.zeros((img_height, img_width, img_channels),
                           dtype=np.uint8)

    #https://www.pythoninformer.com/python-libraries/numpy/numpy-and-images/
    if background_color is not None:
        initial_img[:, :] = background_color

    return initial_img

def run_celullar_automata(state_matrix, image, rules, path, n_cells):
    for j, generation in enumerate(state_matrix[:-1, :]):
        # #if t//100:
        temp_image = Image.fromarray(image, mode='RGB')
        image_name = 'Frame' + str(j+1).zfill(3) + '.jpeg'
        temp_image.save(join(path, image_name))

        new_generation = [rules[tuple([generation[len(generation) - 1],
                                       generation[0], generation[1]])]]
        _ = [new_generation.append(rules[tuple([generation[i - 1], generation[i], generation[i + 1]])]) for i in range(1, n_cells-1)]
        new_generation.append(rules[tuple([generation[len(generation) - 2],
                                           generation[len(generation) - 1], generation[0]])])
        state_matrix[j+1, :] = new_generation
        image[state_matrix == 1] = automata_color


if __name__ == "__main__":

    n_generations = 1024
    #rules numbers can be found here:
    #https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
    rule_number = 18
    background_color = [255, 255, 255]
    automata_color = [255, 0, 0]

    ca_rules = define_rule(rule_number)
    ss = space_states(n_generations)
    n_cells = ss.shape[1]

    path_figures = "~/temp/art/ca/1d/bw"

    # Image size
    width = n_cells
    height = n_generations
    # channels = 1
    channels = 3
    # Create an empty image
    img = create_initial_image(height, width, channels, background_color)
    run_celullar_automata(ss, img, ca_rules, path_figures, n_cells)
