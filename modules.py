''' This program is to Write a function called nfl_wins() that takes a team name (string value) as the input.
The function should return the number of games the team won in the period covered by the data set.
Use the function to assign the number of times the Dallas Cowboys ("Dallas Cowboys") won to cowboys_wins.
Use the function to assign the number of times the Atlanta Falcons won ("Atlanta Falcons") to falcons_wins.
'''
import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(team):
    patriots_wins=0
    for i in nfl:
        if i[2]==team:
            patriots_wins+=1
    return patriots_wins
cowboys_wins=nfl_wins("Dallas Cowboys")
falcons_wins=nfl_wins("Atlanta Falcons")
    
