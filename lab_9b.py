# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:43:10 2024

@author: bmyou
"""

## Brianna Youngblood 

## Simulation: Schelling Model 

## Create an Agent Class

class Agent:
    def __init__(self, type):
        self.type = type
        self.happy = False
        pass
    def happy(self, neighborhood, threshold):
        same_neighbors= sum(1 for n in neighborhood if n == self.type)
        total_neighbors= len(neighborhood)
        if total_neighbors == 0:
            return False
        ratio = same_neighbors / total_neighbors
        return ratio >= threshold
    



## Create a World Class

## Initialize

## Create Loop 

