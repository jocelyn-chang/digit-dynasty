import csv

class Player: 
    # initialize Player object
    def __init__ (self, name, password):
        self.name = name
        self.password = password
        self.level = 0
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
                    self.subtraction = row[3]
                    self.multiplication = row[4]
                    self.division = row[5]
                    self.bosses = row[6]

    # Modify player's data
    def save_info(self):
        player = []

        # Read current info and match with current player
        with open("data.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == self.name and row[1] == self.password:
                    # Update this player's data
                    row[2] = self.addition
                    row[3] = self.subtraction
                    row[4] = self.multiplication
                    row[5] = self.division
                    row[6] = self.bosses
                player.append(row)
        
        # Write the updated/all data back to the CSV
        with open("data.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(player)
    
    # update Player's add high score
    def update_bosses (self, new_bosses_score):
        self.bosses = new_bosses_score
        self.save_info()

    # update Player's add high score
    def update_add (self, new_add_score):
        self.addition = new_add_score
        self.save_info()

    # update Player's mul high score
    def update_mul (self, new_mul_score):
        self.multiplication = new_mul_score
        self.save_info()

    # update Player's div high score
    def update_div (self, new_div_score):
        self.division = new_div_score
        self.save_info()

    # update Player's sub high score
    def update_sub (self, new_sub_score):
        self.subtraction = new_sub_score
        self.save_info()

    # update Player's boss high score
    def update_boss (self, new_sub_score):
        self.bosses = new_sub_score
        self.save_info()

    # get Player's name
    def get_name (self):
        return self.name
    
    # get Player's name
    def get_bosses (self):
        return self.bosses
    
    # get Player's addition score
    def get_add (self):
        return self.addition
    
    # get Player's multiply score
    def get_mul (self):
        return self.multiplication
    
    # get Player's division score
    def get_div (self):
        return self.division
    
    # get Player's subtraction score
    def get_sub (self):
        return self.subtraction
    
    # get Player's boss score
    def get_boss (self):
        return self.bosses