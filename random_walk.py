from random import choice

class Random_Walk():
    '''A class to generate random walks.'''
    def __init__(self, num_points=1000):
        '''initialise random walk attributes.'''
        self.num_points = num_points
        
        #Every walk starts at 0
        self.y_values = [0]
        self.x_values = [0]
        
    def fill_walk(self):
        '''Calculate all the points in the walk.'''
        while len(self.x_values) < self.num_points:
            x_direction =choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            step_x = x_direction*x_distance
            
            y_direction =choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            step_y = y_direction*y_distance            
            
            if step_x==0 and step_y==0:
                continue
        
            next_x = self.x_values[-1] + step_x
            next_y = self.y_values[-1] + step_y
        
            self.x_values.append(next_x)
            self.y_values.append(next_y)
