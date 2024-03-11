# Initialize an empty dictionary to store users
users = {}



# Function to add a new user
def add_user(username, name, age, location):
    users[username] = {'name': name, 'age': age, 'location': location}