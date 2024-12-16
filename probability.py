"Changes the probibility that dice will land on a certain number"
import random
import dice
import temp
class probability:
    def weighted_choice(choices):
        total = temp.total # we start with 0
        r = random.uniform(0, total) # saying from 0 to choice lets say 0 to 5
        upto = 0

        if 0 < r < temp.two_d[i, 1]:
            

        for key in keys:
            if upto + choices[key] > r:
                return key
            upto += choices[key]

            # 1: 20
            # 2: 21-60
# probability to be defined
    def tem_prob(num_choices):
        prob = float(100 / num_choices)

    def get_user_probabilities(num_choices): 
        getSides(self)
        num_choices = dice.getSides()
        prob = float(100 / num_choices)
        prob = round(prob, 2)
        print(prob)

        
    # Get number of choices from user
    num_choices = int(input("Enter the number of choices: "))

    # Get probabilities from user
    probabilities = get_user_probabilities(num_choices)

    # Create choices with weights
    choices = {}
    for i in range(num_choices):
        choices[i + 1] = probabilities[i]

    # Perform weighted random selection
    result = weighted_choice(choices)
    print("The chosen outcome is:", result)
    # Get number of choices from user
    num_choices = int(input("Enter the number of choices: "))

    # Get probabilities from user
    probabilities = get_user_probabilities(num_choices)

    # Create choices with weights
    choices = []
    for i in range(num_choices):
        choices.append((f"Choice {i+1}", probabilities[i]))

    # Perform weighted random selection
    result = weighted_choice(choices)
    print("The chosen outcome is:", result)