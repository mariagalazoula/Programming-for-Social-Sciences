# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:51:47 2018

@author: gy16mg
"""


"""Import all the modules that will be required for our model.
   
   These modules are: matplotlib, csv, Agent_Framework, matplotlib.animation
"""
import matplotlib
import csv
import Agent_Framework as agfr
import matplotlib.animation

##READING THE DATA FOR THE ENVIRONMENT
"""
In this part we will read the data from the in.txt file 
in order to plot the environment.

"""

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
    

num_of_agents = 10
num_of_iterations = 100
agents= []
neighbourhood= 20

#create a list of agents using the agent framework that we created
for i in range(num_of_agents):
   agents.append(agfr.Agent(environment, agents, neighbourhood))

#set the limits of the plot
matplotlib.pyplot.ylim(300, 0)
matplotlib.pyplot.xlim(0, 300)
    

#BASIC ANIMATION
#import operator

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# In this part we will make the agents move, eat and share their store with their neighbours.

carry_on = True

def update(frame_number):
    
    fig.clear() 
    
    matplotlib.pyplot.imshow(environment)
    global carry_on
    
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        
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

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
