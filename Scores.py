from selenium import webdriver

def getDriver(team1: str, team2: str):
    path = r'C:\\Users\\Brad\\Downloads\\chromedriver\\chromedriver'
    driver = webdriver.Chrome(executable_path = path)
    URL = 'https://www.google.com/search?q='

    driver.get(URL +  team1 + '%20vs%20' + team2)

    return driver

def closeDriver(driver):
    driver.close()

def inGame(driver):
    sports = driver.find_element_by_id("sports-app")
    return (((sports.text).split())[5] != "Final")

def getScores(team1: str, team2: str, driver):

    score1 = 0
    score2 = 0

    sports = driver.find_element_by_id("sports-app")
    scores = sports.find_element_by_css_selector("div.imso_mh__ma-sc-cont")
    #print(sports.text)
    if ((sports.text).split())[2] == team1:
        score1 = ((scores.text).split())[0]
    elif ((sports.text).split())[4] == team1:
        score1 = ((scores.text).split())[2]

    if ((sports.text).split())[2] == team2:
        score2 = ((scores.text).split())[0]
    elif ((sports.text).split())[4] == team2:
        score2 = ((scores.text).split())[2]


    """    print(team1, team2)
    print(score1, score2)

    """
    return((int(score1), int(score2)))