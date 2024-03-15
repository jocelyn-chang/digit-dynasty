import random

#inherits stuff from player class
class Question (Player):
    
    def __init__(self, name, level):
        super().__init__(name, level)
        
    def generate_question(self, operation):
        
        