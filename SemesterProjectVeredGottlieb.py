import Draw
import time
import random
#"I hereby certify that this program is solely the result of my own work 
#and is in compliance with the Academic Integrity policy of the course syllabus
#and the academic integrity policy of the CS department.”

#Game Instructions: All instructions on how to play the game will appear in the 
#introduction screen once the play button is pressed. 
#colorList is a list of colors from which a color is selected at random 
#for graphics purposes
def showIntroductionScreen(colorList):
    
    #Introduces the game 
    #when it gets to the end, it gives the user a few seconds to click a key 
    #to continue to the game. if they don't click the instructions 
    #will start displaying again from the beginning
    while not( Draw.hasNextKeyTyped()):
        #make the big text
        Draw.setBackground(Draw.BLACK)
        Draw.setFontSize(48)
        Draw.setFontFamily('Courier New')
        
        #first bit of instructions will show for 2 seconds
        Draw.clear()
        Draw.setColor(random.choice(colorList))
        Draw.string("Can you spot the differences in two \nnearly identical pictures?",50,250)
        Draw.show()
        time.sleep(2)
        
        #show the next bit of instructions in a new color for 4 seconds
        Draw.clear()
        Draw.setColor(random.choice(colorList))
        Draw.string("Click on the Left Image to select a difference ",50,250)
        Draw.show()
        time.sleep(4)
        Draw.clear()
        
        #show the next bit of instructions in a new color for 5 seconds
        Draw.setColor(random.choice(colorList))
        Draw.string("You earn one point for every difference you find \
        \nand that area will light up.\nYou lose a point if it's not a difference \
        \nor if you already clicked that area.\
        \nIf you find all differences before the time \n you earn 5 extra points",\
                    50,250)
        Draw.show() 
        time.sleep(5)
        Draw.clear()
        
        #show last bit of instructions in a new color for 10 seconds
        Draw.setColor(random.choice(colorList))
        Draw.string("You will have ten different puzzles.\nScore 45 points to win.\
        \nGood Luck!!! \nClick any key to begin",50,250)
        Draw.show()   
        time.sleep(10)
        Draw.clear()
        
        Draw.setBackground(Draw.WHITE)
        Draw.setColor(Draw.BLACK)  
        
#the playGame function sets up the general game-play         
def playGame():
       
    #Answer-key of areas of difference locations for each puzzle
    
    
    kitchenPuzzleAnswers = [(225,80,60,60),(170,215,55,55),(300,215,50,50),
                            (140,635,100,75),(505,675,80,60),(645,590,25,50),
                            (505,455,40,40),(445,295,20,25),(645,390,35,35),
                            (442,475,45,45),(200,400,40,40),(585,185,70,40),
                            (565,275,70,75)]
   
    carPuzzleAnswers = [(165,200,50,50),(230,210,50,60),(230,120,50,60),
                        (85,240,75,75),(105,450,90,90),(160,520,80,80),
                        (490,155,45,45),(340,300,50,50),(325,340,80,80),
                        (265,630,45,45),(400,585,60,60)]     
    
    sushiPuzzleAnswers = [(340,46,100,70),(235,70,100,100),(150,230,105,105),
                          (72,307,55,55),(53,365,80,80),(55,470,100,100),
                          (510,510,67,100),(325,515,100,100),(214,705,101,57),
                          (274,650,30,30)]
    
    donutPuzzleAnswers = [(460,90,50,50),(465,195,50,50),(195,220,50,50),
                          (375,470,50,50),(230,560,50,50),(245,670,50,50),
                          (390,625,50,50),(425,670,150,70)]   
    
    cupcakePuzzleAnswers = [(270,135,70,70),(452,70,110,110),(245,240,135,135),
                            (125,520,52,52),(255,490,100,100),(450,410,130,140),
                            (470,635,100,100)]     
    
    vegetablePuzzleAnswers = [(96,102,90,90),(190,150,50,50),(280,240,55,55),
                              (335,205,55,55),(415,320,75,75),(483,230,78,92),
                              (245,490,95,95),(483,75,30,30)]    
    
    breakfastPuzzleAnswers = [(150,300,60,60),(285,285,50,50),(83,493,50,50),
                              (485,430,65,65),(427,597,65,65),(213,625,60,60)]    
    
    cafePuzzleAnswers = [(263,240,65,65),(145,255,65,65),(425,240,85,85),
                         (535,255,45,45),(405,390,120,120),(75,457,45,45)] 
    
    bikePuzzleAnswers = [(160,220,90,90),(283,337,60,60),(130,440,90,90),
                         (455,530,60,60),(493,635,50,50)]
    
    flowerPuzzleAnswers = [(85,155,50,50),(505,265,65,65),(380,345,60,60),
                           (105,530,55,55),(515,595,55,55)]    
    
    #each puzzle with it's left image, right image, list of answer locations, 
    #size of left image
    kitchenPuzzle = [("KitchenPuzzleLeftImage.gif","KitchenPuzzleRightImage.gif"),
                     kitchenPuzzleAnswers,(626,688)]  
    
    carPuzzle = [("carPuzzleLeftImage.gif","carPuzzleRightImage.gif"),
                 carPuzzleAnswers,(487,649)]
    
    sushiPuzzle = [("SushiPuzzleLeftImage.gif","SushiPuzzleRightImage.gif"),
                   sushiPuzzleAnswers,(528,702)]    
    
    donutPuzzle = [("DonutPuzzleLeftImage.gif","DonutPuzzleRightImage.gif"),
                   donutPuzzleAnswers,(525,658)] 
    
    cupcakePuzzle = [("CupcakePuzzleLeftImage.gif","CupcakePuzzleRightImage.gif"),
                     cupcakePuzzleAnswers,(527,698)]    
    
    vegetablePuzzle = [("vegetablePuzzleLeftImage.gif","vegetablePuzzleRightImage.gif"),
                       vegetablePuzzleAnswers,(508,672)]
   
    breakfastPuzzle = [("BreakfastPuzzleLeftImage.gif","BreakfastPuzzleRightImage.gif"),
                       breakfastPuzzleAnswers,(529,699)]    
    
    cafePuzzle = [("CafePuzzleLeftImage.gif","CafePuzzleRightImage.gif"),
                  cafePuzzleAnswers,(524,697)]    
    
    bikePuzzle = [("BikePuzzleLeftImage.gif","BikePuzzleRightImage.gif"),
                   bikePuzzleAnswers,(532,708)]
    
    flowerPuzzle = [("FlowerPuzzleLeftImage.gif","FlowerPuzzleRightImage.gif"),
                    flowerPuzzleAnswers,(529,703)]    
    
    
    #complete list of puzzles
    listPuzzles = [kitchenPuzzle,carPuzzle,sushiPuzzle,
                   donutPuzzle,cupcakePuzzle,vegetablePuzzle,
                   breakfastPuzzle,cafePuzzle,bikePuzzle,flowerPuzzle]
    
    #used to select a random color for backgrounds 
    colorList = [Draw.GRAY,Draw.RED,Draw.GREEN,Draw.BLUE,Draw.CYAN,Draw.MAGENTA,
                 Draw.YELLOW,Draw.ORANGE,Draw.VIOLET,Draw.PINK ]    
    #variables 
    #score for each round
    score = 0 
    #list of scores from each round
    scoreList = []
    
    #score gotten by combining the score recieved from each round 
    totalScore = 0 
    
    #score required to win
    threshHoldWinScore = 45 
    
    #amount of time the player has to solve the first puzzle
    allowableTime = 90
    
    #Introduce the Game to the Audience
    showIntroductionScreen(colorList)
    
    #Show each puzzle, one at a time for allowableTime, which will decrease for 
    #every puzzle as a challenge
    for count in range(len(listPuzzles)):
        scoreList += [showPuzzle( listPuzzles[count][0],listPuzzles[count][1], 
                    allowableTime,listPuzzles[count][2],score)]
        allowableTime -= 5  #change to 5  
    totalScore = sum(scoreList)
        
    #if the actual score meets the score necessary to win, then tell 
    #the user that they've won with the winscreen function
    if totalScore >= threshHoldWinScore:
        winScreen(totalScore,scoreList,colorList)
    else:
        #otherwise tell the user they've lost with the lose screen function
        loseScreen(totalScore, scoreList)
        
#tells the computer which puzzle to display and what to input into the 
#draw everything later 
#it takes as input the puzzle the user is completing. 
#the list of answers for that puzzle
#the amount of time the user will be allowed to complete the game
#the size of the left image of that puzzle
#the score of the user 
def showPuzzle( puzzle, answerList, allowableTime,size,score):
    
    #variables
    #list of answer locations that have been successfully found
    successfulClicks = []
    #ensures that credit for clicking correct answer locations is only given once
    Clicks = {}
    #time that the game started
    start = time.time()  
    #time left for each round.
    remaining = allowableTime - int(time.time() - start)
    #stores the x and y of a users click
    xClick = 0
    yClick = 0  
    numGoodClicks = 0
    #is this click the first time an answer location has been successfully found?
    #starts at false automatically 
    successfulClick = False
    #initial drawing of the screen so the user can see the puzzle and 
    #start clicking on differences (fencepost solution) 
    redrawScreen( puzzle, answerList, successfulClicks, score, remaining,size)
    
    #while there's time left in the round
    while remaining > 0: 
        
        #if the user has clicked
        if Draw.mousePressed(): 
            #store the x and y of that click in the variables
            xClick = Draw.mouseX()
            yClick = Draw.mouseY() 
            
            #check through the list of answer locations
            for click in answerList:
                
                #if the x and y of the users click is within the boundaries
                #of the same one of the answer locations 
                if click[0] <= xClick <= click[0] + click[2] and\
                click[1] <= yClick <= click[1] + click[3]:
                    
                    #if it's already been clicked, don't count as a good click
                    if click in Clicks:
                        Clicks[click] += 1
                        successfulClick = False
                        
                    else: 
                        #if it hasn't been clicked, add it to the dictionary
                        #and count it as a good click
                        Clicks[click] = 1
                        successfulClicks += [click]
                        successfulClick = True 
                    
            #if the user has a good click, earn a point and add one
            #number of good clicks made. reset successfulClick
            if successfulClick:
                score += 1
                numGoodClicks += 1
                successfulClick = False
                
                #if you find all of the differences before time is up, then
                #you get 5 "extra credit points" and you move on to the 
                #next thing                 
                if numGoodClicks == len(answerList):
                    score += 5 
                    return score
                
            #otherwise,lose a point, unless the score is 0, in which case
            #the score remains at 0
            else:
                successfulClick = False
                score -= 1
                if score < 0:
                    score = 0
        #draw the screen using all the information provided from this function
        redrawScreen(puzzle, answerList,successfulClicks, score, remaining,size)
        
        #update the remaining time 
        remaining =  allowableTime - int(time.time() - start)
    #when done, return the score earned for this round
    return score

#does the actual drawing
#it takes as input the puzzle the user is completing. 
#the list of answers for that puzzle
#the list of answer locations the user has found
#the amount of time the user has left to complete the puzzle
#the size of the left image of that puzzle
def redrawScreen(puzzle, answerList,successfulClicks, score, remainingTime,size):
    
    #clear the screen
    Draw.clear()
    #draws the left image
    Draw.picture(puzzle[0], 50,50) 
    #draws the right image
    Draw.picture(puzzle[1],size[0] + 50,50) 
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(24)
    #draws the score earned in each round
    #number of differences left to find and the time remaining
    Draw.string("Score for the round: " + str(score), 1100,0)  
    Draw.string("Number of Differences Left: " 
                + str(len(answerList) - len(successfulClicks)),500 ,0)
    Draw.string("Time Remaining: " + str(remainingTime) ,0 ,0) 
    Draw.setColor(Draw.BLACK)
    #draws the answer locations that have successfully been found
    for answer in successfulClicks:
        Draw.setColor(Draw.GREEN)
        Draw.filledOval(answer[0],answer[1],answer[2],answer[3])  
        Draw.setColor(Draw.BLACK)
    #show everything since the last clear (shows the images, differences found
    # time remaining, and the score) 
    Draw.show() 
 
#Celebrates the User's Win 
#takes as an input the users total score 
#and the list of scores from each round
#colorList is again used for graphics purposes (to choose colors from it for
#the background) 
def winScreen(score,scoreList,colorList):
   
    Draw.clear()
    #black background - to make it look nicer 
    Draw.setBackground(Draw.BLACK)
    #flash a win message with the total score in different colors 10 times 
    for x in range(0, 100 ,10):
        Draw.clear()
        Draw.setColor(random.choice(colorList))
        Draw.setFontSize(72)
        Draw.string("CONGRATULATIONS!\n YOUR TOTAL SCORE WAS " + str(score),50,100)
        time.sleep(.5)
        Draw.show()
        
    #set the color to cyan and show the scores the user
    #recieved for each round
    Draw.setColor(Draw.CYAN)
    Draw.clear()
    for num in range(len(scoreList)):
        Draw.string("for puzzle " + str(num + 1) + " your score was: " 
                    + str(scoreList[num]),0, num * 75) 
    Draw.show()

#gives the users condolences and showed them how they did in each round
#takes as an input the users total score 
#and the list of scores from each round
def loseScreen(totalScore,scoreList):
    #displays the I'm sorry message for 5 seconds
    Draw.clear()
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(48)
    Draw.string("Sorry. " + str(totalScore) + " isn't enough",0,0)
    Draw.show()
    time.sleep(5)
    Draw.clear()
    
    #displays the users scores from each round for 10 seconds
    for num in range(len(scoreList)):
        Draw.string(("puzzle " + str(num + 1) + " score:  " + str(scoreList[num])),0, (50 * num))
    Draw.show()
    time.sleep(10)
    Draw.clear()
    
    
#everything's run in the main function    
def main():
    Draw.setCanvasSize(1500,1000) 
    playGame()   
#runs the code  
main()    

 