import random
from player import Player

#inherits stuff from player class
class Question (Player):
    
    def __init__(self, name, best_game, best_score, add_score, mul_score, div_score, sub_score, games):
        super().__init__(name, best_game, best_score, add_score, mul_score, div_score, sub_score, games)
        
    def generate_question(self, operation):
        
        if operation == '+':
            level = self.get_add()
            
        elif operation == '-':
            level = self.get_sub()
            
        elif operation == '*':
            level = self.get_mul()
            
        elif operation == "/":
            level = self.get_div()
            
            
        if self.level <= 5:
            digits = (1, 9)  # Single-digit numbers    
        elif 5 < self.level <= 10:
            digits = (1, 99)  # Single and double-digit numbers
        elif 10 < self.level <= 15:
            digits = (1, 999)  # Single, double, and triple-digit numbers
        elif self.level > 20:
            digits = (1, 999)
            
        num1 = random.randint(*digits)
        num2 = random.randint(*digits)
    
        # wrtie the question based on the operation given
        question = f"What is {num1} {operation} {num2}?"
    
        return question