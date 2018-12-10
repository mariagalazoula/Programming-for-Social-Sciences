# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:28:53 2018

@author: gy16mg
"""

#Create an Agent class

#I need to make the __init__ do something so that it runs
#class Agent:
#    def __init__(self):
#        pass<- WE NEED THIS TO MAKE IT WORK, SO THAT STH HAPPENS
#        
  
#when we give arguments to the function __init__, later we have to assign values later
#class Agent:
#    def __init__(self,x,y):
#       self.x = random.randint(0,99)
#       self.y = random.randint(0,99)

#this does not work, because later we would need to ASSIGN 
#the x and y to the agent that we created in the model3
#whatever we have in the parenthesis, we have to provide a value for it 

#Create an Agent Class, where we will give the agents all of the 
#attributes that they will need for this model. First, we create the 
#agents by creating an initial function called __init__, where we 
#assign the attributes of the agents, such as the neighbourhood, 
#environment, etc and we also create the functions needed for this model,
#in order to move the agents, to make them eat, to calculate 
#the distances between the agents and to make them share with their neighbours.

import random  

#create the class for the agents:
class Agent:
    
#create the agents and their attributes
    def __init__(self, environment, agents, neighbourhood):
        """
        In this function we give the attributes to the agents.
        
        """
        self.y = random.randint(0,300)
        self.x = random.randint(0,300)
        self.environment = environment
        self.store = 0
        self.agents = agents
        self.neighbourhood = neighbourhood

#function for moving the agents using the Torus, where the modulus operator is used          
    def move(self):
        if random.random()<0.5:
            self.x = (self.x + 1)%300 
        else:
            self.x = (self.x - 1)%300
        
        if random.random()<0.5: 
            self.y = (self.y + 1)%300
        else:
            self.y = (self.y - 1)%300

#function for "eat", where agents can "eat" the environment around them and store 
#depending on the value of the environment
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store +=10
        else:
            self.store = self.environment[self.y][self.x]  
            self.environment[self.y][self.x] -= 10
                       
#function to calculate the distance of two agents using the Pythagorean Theoreum     
    def dist(self, agent):
        return (((self.y-agent.y)**2)+ ((self.x-agent.x)**2))**0.5

#function to share the store with the agent-neighbours
#based on their distance, which should be less than the neighbourhood that we set
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:
            distance= self.dist(agent)
            if distance<= self.neighbourhood:
                sum= self.store + agent.store
                average = sum/2
                self.store= average
                agent.store = average
            else:
                self.store = self.store
                agent.store = agent.store
                
                
      

         
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                