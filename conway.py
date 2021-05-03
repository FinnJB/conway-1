#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:31:37 2021
Provides the ConwayBase class and an implementation of said class.

@author: dkappe
"""

from abc import ABC, abstractclassmethod

import numpy as np

from configs import DYING, REBORN, ALIVE


class ConwayBase(ABC):
    """
    ConwayBase is an abstract base class with all of the Game's logic missing.
    Any class based on it has to implement the methods:
     * update_field()
     * show_field()

    Parameters
    ----------
    start_field : numpy.ndarray
        Simulation field at the start of the Game.

    Properties
    ----------
    start_field: numpy.ndarray
        Simulation field at the start of the Game.
    current_field: numpy.ndarray
        Current state of the Simulation field.
    size: int
        Size of the start_field numpy.ndarray
    shape: (int, int)
        Shape of the start_field numpy.ndarray
    is_empty: bool
        Checks whether there are any points left on the simulation field.
    """
    def __init__(self, start_field: np.ndarray):
        self.start_field = start_field
        self.reset_field()
        self.size = self.current_field.size
        self.shape = self.current_field.shape
        
    @abstractclassmethod
    def update_field(self):
        """
        Class method providing the Game logic. Here the current_field has to be
        updated for the next frame.
        """
        pass
    
    @abstractclassmethod
    def show_field(self) -> np.ndarray:
        """
        Class method returning the image to be displayed. The Image can either
        be a 2D numpy array with shape (width, height) or a 3D numpy array with
        shape (width, height, color), where color are RGB values

        Returns
        -------
        numpy.ndarray
            The image to be drawn.

        """
        pass
    
    def reset_field(self):
        """
        Resets the simulation field to the starting configuration.
        """
        self.current_field = np.array(self.start_field, copy=True)
    
    @property
    def is_empty(self) -> bool:
        """
        Checks and returns, if current_field has no non-zero values.
        """
        return np.sum(self.current_field) == 0


class Conway(ConwayBase):
    def __init__(self, start_field, border:bool = True,
                 fade: tuple = (1, 1, 1), gauss_sigma: tuple = (0, 0, 0)):
        super().__init__(start_field)
        pass
    
    def update_field(self):
        new_field = np.array(self.current_field, copy=True)

        if DYING in self.current_field or REBORN in self.current_field:
            new_field = np.where(new_field == DYING, 0, new_field)
            new_field = np.where(new_field == REBORN, ALIVE, new_field)

        else:
            for (r, c), val in np.ndenumerate(self.current_field):
                neighbors = self.current_field[r - 1:r + 2, c - 1:c + 2]
                count_alive = np.count_nonzero(neighbors)
                count_alive = count_alive - 1 if val > 0 else count_alive

                if val > 0 and (count_alive < 2 or count_alive > 3):
                    new_field[r, c] = DYING
                if val == 0 and count_alive == 3:
                    new_field[r, c] = REBORN
        self.current_field = new_field

    def show_field(self) -> np.ndarray:
        return self.current_field
