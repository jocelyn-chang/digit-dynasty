class Player: 
    def __init__ (self, username, best_game, best_score, add_score, mul_score, div_score, sub_score, games):
        self.username = username
        self.best_game = best_game
        self.best_score = best_score
        self.add_score = add_score
        self.mul_score = mul_score
        self.div_score = div_score
        self.sub_score = sub_score
        self.games = games
    
    def add_game (self, game):
        self.games.append(game)

    def update_add (self, new_add_score):
        self.high_score_add = new_add_score

    #def update_mul (self, new_)