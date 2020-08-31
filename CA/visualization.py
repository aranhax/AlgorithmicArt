#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Aug  2020

Interesting links:
https://www.pythoninformer.com/python-libraries/numpy/numpy-and-images/

"""
from os.path import join
import numpy as np
from PIL import Image


def create_initial_image(img_height, img_width, img_channels,
                         background_color=None):

    initial_img = np.zeros((img_height, img_width, img_channels),
                           dtype=np.uint8)

    if background_color is not None:
        initial_img[:, :] = background_color

    return initial_img

def write_image(image_matrix, write_path, iteration_index):

    temp_image = Image.fromarray(image_matrix, mode='RGB')
    image_name = 'Frame' + str(iteration_index+1).zfill(3) + '.jpeg'
    temp_image.save(join(write_path, image_name))
