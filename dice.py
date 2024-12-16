import random
import time
''' D6: Dice with 6 Sides
    1. Random Number Gennerators
        - Needs to be on a timed basis how fast do dice roll
            > The amount of rolling decreases as the dice looses energy due to friction
            > The time that dice roll is diffrent so the numbers should gennerate random for diffrent durations of time. 
        - Needs to show what number it is on
    2. Saves to Mongo DB
    3. Gets implemented into the graph
'''
""" I want to use the threading module to make it slow down over time
    The dice will have numbers on the screen that will at first be fast but then be slower and slower until it lands on the final random number.
    """

class dice:
    """ Have """
    def __init__(self, sides = 6, lower_time = 5, upper_time = 15): #Initlizes the programs data
        self.sides = sides
        self.lower_time = lower_time
        self.upper_time = upper_time

    #Get Commands:
    def getSides(self):
        return self.sides
    def getLowerTime(self):
        return self.lower_time
    def getUpperTime(self):
        return self.upper_time

    
    def roll(self):
        return random.randint(1, self.getSides())
    
    def decay(self): # rolls the dice
# This function is used to decrease how fast the dice rolls
        for x in range(random.randint(self.lower_time, self.upper_time)): # how many times will it roll
            print(self.roll())
            waitTime = random.uniform(.4, .2) - (0.05 * x) # first roll will start either at 
            if waitTime < 0:
                waitTime = 0.1
            time.sleep(waitTime)
        time.sleep(.5)
        print("Final roll")
        print(self.roll())
            



        
        

