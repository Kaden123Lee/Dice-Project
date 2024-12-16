from dice import dice
import random
my_dice = dice() # creates an instance of the class 
num_choices = my_dice.getSides()
prob = float(100 / num_choices)
prob = round(prob, 2)
print(prob)
two_d = []  # [number] & [probability]
total = 0
thing = True
for i in range(1, my_dice.getSides() + 1): # goes through and creates a 2d array
    two_d.append([i, prob])
for i in range(len(two_d)):
    total += two_d[i][1]
amount = 0
r = random.uniform(0, total)
temp_total = 0
for i in range(len(two_d)):
    temp_total += two_d[i][1]
    if r <= temp_total:
        print(f"The number is {two_d[i]}: Real number {r}")
        break

    else: 
        amount += 1
        temp_total += two_d[i][0]

    print(f'Amount + 1: Real number {r}')

    
    



print(two_d)
print(f"{total:.2f}")
        


