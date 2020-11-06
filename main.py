from playsound import playsound
import Scores

team1 = input("enter team1: ")
team2 = input("enter team2: ")

driver = Scores.getDriver(team1, team2)
score1 = 0
score2 = 0

current = "yellow"

while Scores.inGame(driver):
    for i in range(60):
        score1, score2 = Scores.getScores(team1, team2, driver)
        print(team1, team2)
        print(score1, score2)
        input("Press enter:")

#playsound('myfile.wav')
Scores.closeDriver(driver)