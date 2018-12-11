### GEOGM Programming for Social Sciences: Core Skills - Assignment 1 

This is the repository for the first assignment in GEOGM Programming for Social Sciences: Core Skills, as part of the Integrated MSc and PhD in Data Analytics and Society that I am currently enrolled in. It consists of the code of the final agent-based model that was created during the practicals of this module. 

### DESCRIPTION

In this assignment we are required to create an agent-based model. We create 10 agents by giving them various attributes such as: their coordinates, the environment they move in, the other agents and their neighbourhood. The agents move freely in the environment, however, this movement is defined by a random number that is generated in each iteration. The environment is provided in the practicals, in the form of a txt file, which can be found in the repository as well (in.txt). 

### FURTHER DETAILS

* The agents are aware of the other agents and the environment that they are in. 
* The agents are assigned random coordinates at first, generating the coordinated randomly from 0 to 300.
* The agents can "eat" from the environment and this value is in their store afterwards. 
* The distance between two agents can also be calculated so that the agents will be aware of whether other agents are in their neighbourhood. 
* In the class **Agent_Framework.py** the agents are assigned all of their attributes and several functions are defined, such as the functions 'move', *eat*, *dist*, *share_with_neighbours*. 
* In the **Final_model.py**, the final code of the model can be found. 
* Finally, a gif file of the animation can be found in the repository, along with a picture of the environment when the data from the txt file was initially read. 
