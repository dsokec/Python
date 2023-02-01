# Sve o Python List
# https://docs.python.org/3/tutorial/datastructures.html

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Ispis
dirtyDozen = [fruits + vegetables]
#print(dirtyDozen)
#print(dirtyDozen[0])
#print(dirtyDozen[1]) IndexError: list index out of range

# Provjeri Quiz 5 - dan 4 - video 45-46
#print(dirtyDozen[0][1]) It works
#print(dirtyDozen[1][0]) Error
#print(dirtyDozen[1][2]) Error






# USA

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#print(states_of_america)
#print(states_of_america[2])
#print(states_of_america[0])
#print(states_of_america[-1])
#print(states_of_america[-3])

#states_of_america[1] = "Pencilvania"
#print(states_of_america[1])

#states_of_america.append("DinoSokecLand")
#print(states_of_america)

#states_of_america.extend(["XYLand", "Jack Bauer Land"])
#print(states_of_america)

#print(len(states_of_america))

# print(states_of_america[50]) IndexError: list index out of range

# Greska
# numOfStates = len(states_of_america)
# print(states_of_america[numOfStates-1])