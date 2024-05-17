# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:43:10 2024

@author: bmyou
"""

## Brianna Youngblood 

## Simulation: Schelling Model 

from numpy import random, mean 

## create parameters

params = {'world_size': (10,10),
          'num_agents': 80, 
          'same_pref': 0.4,
          'max iter': 50,
          'out_path': r'C:\Users\bmyou\OneDrive\Documents\GitHub\simulation'}

## Create Agent Class

class Agent:
    def __init__(self, worl, kind, same):
        self.world = world
        self.kind = kind
        self.same = same
        self.location = None
        pass
    
    def move(self):
        happy= self.satisfied()
        
        if not happy: 
            vacancies= self.world.find_vacant(return_all=True)
            for patch in vacancies: 
                i_moved= False
                if will_i_like_it is True:
                    self.world.grid[self.location] = None
                    self.location = patch
                    self.world.grid[patch] = self
                    i_moved = True
                    return 1 
                if not i_moved: 
                    return 2
            else:
                return 0
    
    def satisfied(self, loc=False, neighbor_check=False):
        if not loc: 
            starting_loc = self.location
        else:
            starting_loc = loc 
            
        neighbor_patches = self.locate_neighbors(starting_loc)
        neighbor_agents = [self.world.grid[patch] for patch in neighbor_patches]
        neighbor_kinds= [agent.kind for agent in neighbors_agents if agent is not None]
        num_like_me = sum([kind == self.kind for kind in neighbor_kinds])
        
        if neighbor_check:
            return[kind==self.kind for kind in neighbor_kinds]
        if len(neighbor_kinds) == 0:
            return False
        
        perc_like_me = num_like_me / len(neighbor_kinds)
        
        if perc_like_me < self.same_pref:
            return False
        else:
            return True
    
    def locate_neighbors(self, loc):
        include_corners = True
        
        x, y = loc
        cardinal_four = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        if include_corners: 
            corner_four = [(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]
            neighbors = cardinal_four + corner_four
        else:
            neighbors = cardinal_four
            
        x_max = self.world.params['world_size'][0] - 1
        y_max = self.world.params['world_size'][1] - 1

        def _edge_fixer(loc):
            x, y = loc
            if x < 0:
                x = x_max
            elif x > x_max:
                x = 0
                
            if y < 0:
                y = y_max
            elif y > y_max:
                y = 0
                
            return(x,y)
        
        neighbors = [_edge_fixer(loc) for loc in neighbors]
        return neighbors
    
## Create a World Class
class World: 
    def __init__(self, ):
    def build_grid(self): 
    def build_agents(self):
    def init_world(self):
    def find_vacant(self):
    def report_integration(self):
    def report(self)L:
    def run(self):
        

## Initialize

## Create Loop 

