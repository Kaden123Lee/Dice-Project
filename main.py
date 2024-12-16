import dice
"""
Date: 11/14/2024
Total Time: 1 hour

"""
class main:
    def __init__(self):
        pass
    
    def main():
        dice_number = input("""
        Class Main:
        Class D6: 
        Class D10:
        Class D20:
        Class D12:
        Class D8:
""")
        dice6 = dice.dice(6)
        dice10 = dice.dice(10)
        dice20 = dice.dice(20)
        dice12 = dice.dice(12)
        dice8 = dice.dice(8)
        dice6.decay()

    if __name__ == "__main__":
        main()
        
          