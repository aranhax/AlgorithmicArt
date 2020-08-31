#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Aug  2020

Rules numbers can be found here:
https://mathworld.wolfram.com/ElementaryCellularAutomaton.html

"""
from pathlib import Path
from os.path import join
from wolfram import run_cellular_automata
from visualization import create_initial_image


if __name__ == "__main__":

    n_generations = 1024
    rule_number = 18
    background_color = [0, 0, 0]
    #automata_color = [255, 0, 0]

    home = str(Path.home())
    path_figures = join(home, "temp/art/ca/1d/bw")

    # Image size
    width = (n_generations * 2) + 1
    height = n_generations
    channels = 3

    # Create an empty image
    img = create_initial_image(height, width, channels, background_color)
    # run the algorithm
    run_cellular_automata(img, rule_number, n_generations, path_figures)
