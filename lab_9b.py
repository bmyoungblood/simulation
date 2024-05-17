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
    def __init__(self, params):
        assert(params['world_size'][0]*params['world_size'][1] > params['num_agents']), 'Grid too small'
        self.params = params
        self.reports = {}
        
        self.grid = self.build_grid(params['world_size'])
        self.agents = self.build_agents(params['num_agents'], params['same_pref'])
        
        self.init_world()
        
    def build_grid(self, world_size):
        locations= [(i,j) for i in range(world_size[0]) for j in range(world_size[1])]
        return {l:None for l in locations}
    
    def build_agents(self, num_agents, same_pref):
        def kind_picker(i):
            if i < round(num_agents/2):
                return 'red'
            else:
                return 'blue'
            
        agents= [Agent(self, kind_picker, same_pref) for i in range(num_agents)]
        random.shuffle(agents)
        return agents
        
    def init_world(self):
        for agent in self.agents:
            loc= self.find_vacant()
            self.grid[loc] = agent
            agent.location = loc
            
        assert(all([agent.location is not None for agent in self.agents])), "Agents are homeless!"
        assert(sum([occupant is not None for occupant in self.grid.values()])== self.params['num_agents']), "Mismatch!"
        
        self.reports['integration']=[]
        
    def find_vacant(self):
        empties=[loc for loc, occupant in self.grid.items() if occupant is None]
        if return_all:
            return empties
        else: 
            choice_index = random.choice(range(len(empties)))
            return empties[choice_index]
        
    def report_integration(self):
        diff_neighbors = []
        for agent in self.agents:
            diff_neighbors.append(sum(
                [not a for a in agent.satisfied(neighbor_check=True)]
                        ))
        self.reports['integration'].append(round(mean(diff_neigbors), 2))

    def run(self):
        log_of_happy= []
        log_of_moved= []
        log_of_stay= []
        
        self.report_integration()
        log_of_happy.append(sum([a.satisfied() for a in self.agents]))
        log_of_moved.append(0)
        log_of_stay.append(0)
        
        for iteration in range(self.params['max_iter']):
            random.shuffle(self.agents)
            move_results = [agent.move() for agent in self.agents]
            self.report_integration()
            
            num_happy_at_start = sum([r==0 for r in move_results])
            num_moved = sum([r==1 for r in move_results])
            num_stayed_unhappy= sum([r==2 for r in move_results])
            
            log_of_happy.append(num_happy_at_start)
            log_of_moved.append(num_moved)
            log_of_stay.append(num_stayed_unhappy)
        

## Initialize

world = World(params)
world.run()

 

