import random
from Player import Player

#inherits stuff from player class
class Question:

    def __init__(self, player):
        self.player = player

    def generate_question(self, operation):
        if operation == '+':
            level = self.player.get_add()
            
            
        if operation == '-':
            #level_tuple = self.player.get_sub()  # This is a tuple
            level = int(self.player.get_sub())
            #level = int(level_tuple[0]) 
            print(level)
            
            if level <= 5:
                digits = (1, 9) # single digits
            else:
                digits = (1, 50) #double digits
            
            num1 = random.randint(*digits)
            num2 = random.randint(*digits)

            # Ensure b <= a for subtraction
            if num2 > num1:
                num1, num2 = num2, num1  # Swap values
            
            ans = num1 - num2

        elif operation == '*':
            if level <= 5:
                digits = (2, 4)  # Single-digit numbers    
            elif 5 < level <= 10:
                digits = (2, 7)  # Single and double-digit numbers
            elif 10 < level <= 15:
                digits = (2, 10)  # Single, harder double-digit numbers
            elif 15 < level <= 20:
                digits = (2, 15)  # Single, and all double-digit numbers
            elif 20 < level <= 25:
                digits = (2, 20)  # Single, double, and easier triple-digit numbers
            elif 25 < level <= 30:
                digits = (2, 25)  # Single, double, and harder triple-digit numbers
            elif level > 30:
                digits = (2, 30)
            
            num1 = random.randint(*digits)
            num2 = random.randint(*digits)

            if num2 == num1:
                if num2 == 1:
                    num2+=1
                else:
                    num2-=1
            return [num1, num2]
        
        elif operation == "/":
            level = int(self.player.get_div())
            if level <= 5:
                digits = (1, 2)  # Dividing numbers from 4 and below
            elif 5 < level <= 10:
                digits = (1, 4)  # Dividing numbers from 16 and below
            elif 10 < level <= 15:
                digits = (1, 6)  # Dividing numbers from 36 and below
            elif 15 < level <= 20:
                digits = (1, 8)  # Dividing numbers from 64 and below
            elif 20 < level <= 25:
                digits = (1, 10)  # Dividing numbers from 100 and below
            elif 25 < level <= 30:
                digits = (1, 12)  # Dividing numbers from 144 and below

            num1 = random.randint(*digits)
            num2 = random.randint(*digits)

            dividend = num1 * num2
            quotient = dividend / num1
            question = f"{dividend} / {num1}?"

            return [int(quotient), question]

        # wrtie the question based on the operation given
        question = f"{num1} {operation} {num2}?"
    
        return [question, ans]