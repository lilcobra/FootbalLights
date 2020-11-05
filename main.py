import Scores

team1 = input("enter team1: ")
team2 = input("enter team2: ")


score1 = 0
score2 = 0

score1, score2 = Scores.getScores(team1, team2)
print(team1, team2)
print(score1, score2)

