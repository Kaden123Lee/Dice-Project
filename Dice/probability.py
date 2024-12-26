from dice import dice
import random

class Probability:
    def __init__(self, total = 0):
        self.total = total
        self.num_choices = dice().getSides()
        self.two_d = []
        self.probability_per_choice = round(100 / self.num_choices, 2)
        self.populate_two_d() 
# ------------------------------------------------------
    def get_total(self):
        total = 0
        for i in range(len(self.two_d)):
            total += self.two_d[i][1]
        return total
# ---------------------------------------------------
    def get_num_choices(self):
        return self.num_choices 
# -------------------------------------------------     
    def populate_two_d(self): # used in the __init__ function to create the two d array with the number choices and other stuff
        """Populate the 2D array with numbers and their probabilities."""
        for i in range(1, self.num_choices + 1):
            self.two_d.append([i, self.probability_per_choice])
# ----------------------------------------------------------------
    def generate_random_number(self):
        """Simulate a random roll and return the result."""
        r = random.uniform(0, self.get_total())
        temp_total = 0
        for row in self.two_d:
            temp_total += row[1]
            if r <= temp_total:
                return row[0], r
# --------------------------------------------------------------
    def display(self):
        """Print details of the 2D array and the total probability."""
        print("2D Array (Number and Probability):", self.two_d)
        print(f"Total Probability: {self.get_total():.2f}")
# -------------------Change Prob------------------------------------------------
def probability_change(self):
    """change = input("What Number would you like to change: ")
    if isinstance(change, int):
        if change > and change < self.num_choices:"""
    pass 
            
# Example Usage
prob = Probability()
print(f"Number of Choices: {prob.get_num_choices()}")
print(f"Probability Per Choice: {prob.probability_per_choice}%")
result, random_value = prob.generate_random_number()
print(f"Generated Number: {result}, Random Value: {random_value}")
prob.display()
   