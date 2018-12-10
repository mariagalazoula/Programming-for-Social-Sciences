# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:54:07 2018

@author: gy16mg
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:51:47 2018

@author: gy16mg
"""

##PRACTICAL COMMUNICATION
#DATA INPUT
#import pandas as pd
import matplotlib

#change the working directory

##READING THE DATA FOR THE ENVIRONMENT
import csv

f = open('in.txt', newline='')

reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#create the environment initially as an empty list
environment = []
#read each row in the reader 
for row in reader:
    #create an empty list for all the values in each row
    rowlist = []    
    #for each of the rows read the values and write them in the list above
    for value in row:
        #fill the empty rowlist with values from each one of the rows
        rowlist.append(value)
    #fill the environment with the rowlists each time    
    environment.append(rowlist)
   #we have to close the reader now that we are done 
f.close

#create the plot for the environment
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

##CREATE AGENTS FROM AGENT_FRAMEWORK

#we import the file that we have created the agent class inside        
import Agent_Framework as agfr
import matplotlib.animation

num_of_agents = 10
num_of_iterations = 100
agents= []
neighbourhood= 20

#create a list of agents using the agent framework that we created
for i in range(num_of_agents):
    agents.append(agfr.Agent(environment, agents, neighbourhood))

#move the agents through the framework (each agent for the number of iterations)
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

#set the limits of the plot
matplotlib.pyplot.ylim(300, 0)
matplotlib.pyplot.xlim(0, 300)
#plot each agent through a loop
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#show the plot
matplotlib.pyplot.show()
     
#make the agents move and eat through the file agent framework
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#see how much store each of the agents has        
          
#for j in range(num_of_iterations):
#   for i in range(num_of_agents):
#       agents[i].move()  
#       agents[i].eat()
#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#show the plot
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()       

#BASIC ANIMATION
#import operator

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)

# Make the agents.

carry_on = True

def update(frame_number):
    
    fig.clear() 
    
    matplotlib.pyplot.imshow(environment)
    global carry_on
    
    for i in range(num_of_agents):
        agents[i].move()
        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i].x,agents[i].y)
        
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1    

#the environment has to be shown right after the fig.clear()
#otherwise, in each iteration, the environment will be cleared as well
#and therefore, we will not be able to see it


#matplotlib.pyplot.imshow(environment)
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()      

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        