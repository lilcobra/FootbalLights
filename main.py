from playsound import playsound
import Scores


if __name__ == '__main__':
    line = 0.0
    if input("H2H or line: ") == "line":
        line = float(input("enter the line: "))
    team1 = input("enter your team: ")
    team2 = input("enter the opposition team: ")

    driver = Scores.getDriver(team1, team2)
    score1 = 0
    score2 = 0

    current = 0
    playsound('Amber.mp3')

    while Scores.inGame(driver):
        for i in range(60):
            score1, score2 = Scores.getScores(team1, team2, driver)
            if (score1 + line) > score2:
                if current != 1:
                    playsound('Green.mp3')
                    current = 1
            elif (score1 + line) == score2:
                if current != 0:
                    playsound('Amber.mp3')
                    current = 0
            else:
                if current != -1:
                    playsound('Red.mp3')
                    current = -1


    Scores.closeDriver(driver)