class Player: 
    # initialize Player object
    def __init__ (self, name, best_game, best_score, add_score, mul_score, div_score, sub_score, games):
        self.name = name
        self.best_game = best_game
        self.best_score = best_score
        self.add_score = add_score
        self.mul_score = mul_score
        self.div_score = div_score
        self.sub_score = sub_score
        self.games = games
    
    # add game to list of Player's game
    def add_game (self, game):
        self.games.append(game)

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
    
    # get Player's games
    def get_games(self):
        return self.games
    
    # get Player's best game
    def get_best_game (self):
        return self.best_game
    
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
    

    
    
