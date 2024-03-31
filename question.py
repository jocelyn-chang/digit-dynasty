import random
from Player import Player

#inherits stuff from player class
class Question:
    """
    A class to generate arithmetic questions based on the player's level.

    Attributes:
        player (Player): The player for whom the question is being generated.
    """

    def __init__(self, player):
        """
        Initializes the Question object with a player.

        Args:
            player (Player): The player for whom the question is being generated.
        """
        self.player = player

    def generate_question(self, operation):
        """
        Generates an arithmetic question based on the player's level and the specified operation.

        Args:
            operation (str): The arithmetic operation for the question ('+', '-', '*', '/', or 'emperor').

        Returns:
            list: A list containing the question as a string and the answer as an integer or float.
        """
        if operation == '+':
            level = int(self.player.get_add())
            if level < 5: # For single digit addition
                num1 = random.randint(1, 9)
                num2 = random.randint(1, 9)
            elif level < 10:
                num1 = random.randint(1, 49)
                num2 = random.randint(1, 49)
            else: # For double digit addition
                num1 = random.randint(1, 99)
                num2 = random.randint(1, 99)

            ans = num1 + num2
            q = str(num1) + " + " + str(num2) + " = ?"
            return [q, ans]
            
            
        elif operation == '-':
            level = int(self.player.get_sub())
            
            if level <= 5:
                digits = (1, 9) # single digits   
            elif level <=10:
                digits = (1, 20)
            else:
                digits = (1, 50) #double digits
            
            num1 = random.randint(*digits)
            num2 = random.randint(*digits)

            # Ensure b <= a for subtraction
            if num2 > num1:
                num1, num2 = num2, num1  # Swap values
            
            ans = num1 - num2

        elif operation == '*':
            level = int(self.player.get_mul())
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
        
        #Arithmetic Emperor Questions
        else:
            operandSymbols = ['+', '-', '*', '/']

            level = int(self.player.get_bosses())
            if level <= 5:
                digits = (1, 3)   
            elif 5 < level <= 10:
                digits = (1, 4)  
            elif 10 < level <= 15:
                digits = (1, 5) 
            elif 15 < level <= 20:
                digits = (1, 6) 
            elif 20 < level <= 25:
                digits = (1, 7)
            elif 25 < level <= 30:
                digits = (1, 8) 
            elif level > 30:
                digits = (1, 9)

            equationFound = False
            while True:
                num_operands = random.randint(2, 4)  # Random number of operands
                operands = random.choices(operandSymbols, k=num_operands)  # Randomly select operands
                numbers = [random.randint(digits[0], digits[1]) for _ in range(num_operands + 1)]  # Generate random numbers
                
                for i in range (len(operands)):
                    if operands[i] == '/':
                        if numbers[i]%numbers[i + 1] == 0:
                            equationFound = True
                        else:
                            equationFound = False
                            break

                if equationFound:
                    break

            expression = ' '.join([f'{num} {op}' for num, op in zip(numbers[:-1], operands)]) + f' {numbers[-1]}'
            result = eval(expression)
            return [expression, result]

        # wrtie the question based on the operation given
        question = f"{num1} {operation} {num2}?"
    
        return [question, ans]