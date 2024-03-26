import csv

class Player: 
    # initialize Player object
    def __init__ (self, name, password):
        self.name = name
        self.password = password
        self.addition = 0
        self.subtraction = 0
        self.multiplication = 0
        self.division = 0
        self.bosses = 0
    
        # Function to load a previous player's information
    def load_player(self):
        with open("data.csv", newline = '') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                username, password = row[0], row[1]

                if username == self.name and password == self.password:
                    self.addition = row[2]
                    self.subtraction = row[3],
                    self.multiplication = row[4]
                    self.division = row[5]
                    self.bosses = row[6]

    # add game to list of Player's game
    def add_game (self, game):
        self.games.append(game)

    # set Player's password
    def set_password (self, password):
        self.password = password

    # update Player's add high score
    def update_add (self, new_add_score):
        self.add_score = new_add_score

    # update Player's mul high score
    def update_mul (self, new_mul_score):
        self.mul_score = new_mul_score

    # update Player's div high score
    def update_div (self, new_div_score):
        self.div_score = new_div_score

    # update Player's sub high score
    def update_sub (self, new_sub_score):
        self.sub_score = new_sub_score

    # get Player's name
    def get_name (self):
        return self.name
    
    # # get Player's games
    # def get_games(self):
    #     return self.games
    
    # # get Player's best game
    # def get_best_game (self):
    #     return self.best_game
    
    # get Player's addition score
    def get_add (self):
        return self.add_score
    
    # get Player's multiply score
    def get_mul (self):
        return self.mul_score
    
    # get Player's division score
    def get_div (self):
        return self.div_score
    
    # get Player's subtraction score
    def get_sub (self):
        return self.sub_score
    

    
    
