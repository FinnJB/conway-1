#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:25:58 2021
Provides a few Objects to play with and a function simplifing placing an object
onto a simulation field.

@author: dkappe
"""
import numpy as np


def insert_pattern(base, pattern, offset=None):
    """
    Takes a base simulation field and places a given pattern with an offset
    onto it. When offset is None, the object is placed into the middle

    Parameters
    ----------
    base : numpy.ndarray
        The base simulation field. Can already hold objects.
    pattern : numpy.ndarray
        The pattern to be placed. Should fit onto the simulation field
    offset : (offset_x, offset_y), optional
        offset in the x and y directions, from the middle. The default is None.

    Raises
    ------
    ValueError
        Error is raised, if the pattern does not fit onto the simulation field.

    Returns
    -------
    field : TYPE
        The simulation field with the pattern placed.
    """
    (base_rows, base_columns) = base.shape
    y_base = base_rows // 2
    x_base = base_columns // 2

    (pat_rows, pat_columns) = np.array(pattern).shape
    y_pat = pat_rows // 2
    x_pat = pat_columns // 2

    row_start = y_base - y_pat
    column_start = x_base - x_pat

    if offset is not None:
        row_start += offset[0]
        column_start += offset[1]

    row_end = row_start + pat_rows
    column_end = column_start + pat_columns

    try:
        base[row_start:row_end, column_start:column_end] = pattern
    except ValueError as ve:
        print(ve)
    return base


ALIVE = 0x00CC00
REBORN = 0x00FF00
DYING = 0x005000

BLINKER = [[ALIVE, ALIVE, ALIVE]]

BEACON = [[ALIVE, ALIVE, 0, 0],
          [ALIVE, ALIVE, 0, 0],
          [0, 0, ALIVE, ALIVE],
          [0, 0, ALIVE, ALIVE]]

PULSER = [[ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE],
          [ALIVE, 0, ALIVE, ALIVE, ALIVE, ALIVE, 0, ALIVE],
          [ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE, ALIVE]]

GOSPER = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ALIVE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ALIVE, 0, ALIVE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ALIVE, ALIVE, 0, 0, 0, 0, 0, 0, ALIVE, ALIVE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ALIVE, ALIVE],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ALIVE, 0, 0, 0, ALIVE, 0, 0, 0, 0, ALIVE, ALIVE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ALIVE, ALIVE],
    [ALIVE, ALIVE, 0, 0, 0, 0, 0, 0, 0, 0, ALIVE, 0, 0, 0, 0, 0, ALIVE, 0, 0, 0, ALIVE, ALIVE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ALIVE, ALIVE, 0, 0, 0, 0, 0, 0, 0, 0, ALIVE, 0, 0, 0, ALIVE, 0, ALIVE, ALIVE, 0, 0, 0, 0, ALIVE, 0, ALIVE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ALIVE, 0, 0, 0, 0, 0, ALIVE, 0, 0, 0, 0, 0, 0, 0, ALIVE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ALIVE, 0, 0, 0, ALIVE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ALIVE, ALIVE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

BEEHIVE = [[0, ALIVE, ALIVE, 0],
           [ALIVE, 0, 0, ALIVE],
           [0, ALIVE, ALIVE, 0]]
