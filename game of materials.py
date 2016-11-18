import pygame, sys, glob, random, time                                          #imports
from pygame.locals import *                                                     #more imports
pygame.init()                                                                   #intializing

panel = 0 #I Know, global variable :(
num2 = 0
diff = 1000

#Functions
def resize(name):
    '''
    (string) -> dimensions (x,y)
    preconditions: name is a variable representing an image.
    Changes the size of all the characters so that they are the same and
    properly fit the screen.
    '''
    new_size = pygame.transform.scale(name, (400, 200))
    return new_size

def nextVals ():
    global panel
    global num2
    num1 = random.randint(0,9)
    while (num1 + 1 == panel):
        num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    while (num2 == num1):
        num2 = random.randint(0,9)
    panel = num1 + 1

def change(last, TF):
    global diff
    if last == 0:
        last = pygame.time.get_ticks()
    now = pygame.time.get_ticks()
    if now - last >= diff or TF == True:
        last = now
        nextVals()
    return last


#*************************************************************************************************************************************************#
#Initializations
screen = pygame.display.set_mode((600, 627))                                   #sets the screen and the size
pygame.display.set_caption('Game of Materials')                                     #names the game El Presidente

background = pygame.image.load('img/lecturehall.png')
background = pygame.transform.scale(background,(600, 627))

student = pygame.image.load('img/attentive.png')
student = pygame.transform.scale(student,(50,50))

sleeper = pygame.image.load('img/sleeper.png')
sleeper= pygame.transform.scale(sleeper,(50,50))

keener = pygame.image.load('img/keener.png')
keener= pygame.transform.scale(keener,(50,50))

Morgan = pygame.image.load('img/morgan.png')
Morgan = pygame.transform.scale(Morgan,(20,20))


impact_font = pygame.font.SysFont('impact', 30)
Score = impact_font.render('Score:', 1, (255,0,0))
Clock = impact_font.render('Time:', 1, (255, 0, 0))

score = 0
timer = 60

white = 255,255,255

Xvals = [100, 450, 60, 500, 190, 280, 380, 470, 220, 160]
Yvals = [100, 100, 365, 365, 355, 280, 215, 190, 185, 100]

last = 0

T = True
F = False


pygame.time.set_timer(USEREVENT+1, 1000)

clock = pygame.time.Clock()

#*************************************************************************************************************************************************#
#main code

while 1:

    mouse_x,mouse_y = pygame.mouse.get_pos()                                    #determines the coordinates of the curser on the screen
    for event in pygame.event.get():                                            #detects every event for every tick

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:#game exits when escape button is pressed
                    pygame.quit(); sys.exit()
                if event.type == USEREVENT+1 and panel in range (0,11) and timer > 0:
                    timer -= 1
    scoreS = str(score)
    TimeS = str(timer)
    ScoreVal = impact_font.render(scoreS, 1, (255,0, 0))
    ClockVal = impact_font.render(TimeS, 1, (255, 0, 0))

    if timer <= 0:
        panel = 100

    if panel == 0:
        screen.fill(white)                                                      #background
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(student, (100,100))
        screen.blit(student, (450,100))
        screen.blit(student, (60,365))
        screen.blit(student, (500,365))
        screen.blit(student, (190,355))
        screen.blit(student, (280,280))
        screen.blit(student, (380,215))
        screen.blit(student, (470,190))
        screen.blit(student, (220,185))

        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))

        pygame.display.flip()                                                   #displays screen and images

        last = change(last, F)



    if panel == 1:

        screen.fill(white)                                                      #background
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(sleeper, (100,100))
        screen.blit(student, (450,100))
        screen.blit(student, (60,365))
        screen.blit(student, (500,365))
        screen.blit(student, (190,355))
        screen.blit(student, (280,280))
        screen.blit(student, (380,215))
        screen.blit(student, (470,190))
        screen.blit(student, (220,185))
        screen.blit(student, (160,100))
        screen.blit(keener, (Xvals[num2], Yvals[num2]))

        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (100, 150) and mouse_y in range (100, 150):
            score += 1
            last = change(last, T)

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (Xvals[num2], Xvals[num2]+50) and mouse_y in range (Yvals[num2], Yvals[num2]+50):
            score -= 1
            last = change(last, T)


        pygame.display.flip()                                                   #displays screen and images

        last = change(last, F)

    if panel == 2:
        screen.fill(white)                                                      #background
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(student, (100,100))
        screen.blit(sleeper, (450,100))
        screen.blit(student, (60,365))
        screen.blit(student, (500,365))
        screen.blit(student, (190,355))
        screen.blit(student, (280,280))
        screen.blit(student, (380,215))
        screen.blit(student, (470,190))
        screen.blit(student, (220,185))
        screen.blit(student, (160,100))
        screen.blit(keener, (Xvals[num2], Yvals[num2]))

        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (450, 500) and mouse_y in range (100, 150):
            score += 1
            last = change(last, T)

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (Xvals[num2], Xvals[num2]+50) and mouse_y in range (Yvals[num2], Yvals[num2]+50):
            score -= 1
            last = change(last, T)

        pygame.display.flip()                                                   #displays screen and images

        last = change(last, F)

    if panel == 3:

        screen.fill(white)                                                      #background
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(student, (100,100))
        screen.blit(student, (450,100))
        screen.blit(sleeper, (60,365))
        screen.blit(student, (500,365))
        screen.blit(student, (190,355))
        screen.blit(student, (280,280))
        screen.blit(student, (380,215))
        screen.blit(student, (470,190))
        screen.blit(student, (220,185))
        screen.blit(student, (160,100))
        screen.blit(keener, (Xvals[num2], Yvals[num2]))

        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (60, 110) and mouse_y in range (365, 415):
            score += 1
            last = change(last, T)

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (Xvals[num2], Xvals[num2]+50) and mouse_y in range (Yvals[num2], Yvals[num2]+50):
            score -= 1
            last = change(last, T)

        pygame.display.flip()                                                   #displays screen and images

        last = change(last, F)

    if panel == 4:

        screen.fill(white)                                                      #background
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(student, (100,100))
        screen.blit(student, (450,100))
        screen.blit(student, (60,365))
        screen.blit(sleeper, (500,365))
        screen.blit(student, (190,355))
        screen.blit(student, (280,280))
        screen.blit(student, (380,215))
        screen.blit(student, (470,190))
        screen.blit(student, (220,185))
        screen.blit(student, (160,100))
        screen.blit(keener, (Xvals[num2], Yvals[num2]))

        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (500, 550) and mouse_y in range (365, 415):
            score += 1
            last = change(last, T)

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (Xvals[num2], Xvals[num2]+50) and mouse_y in range (Yvals[num2], Yvals[num2]+50):
            score -= 1
            last = change(last, T)

        pygame.display.flip()                                                   #displays screen and images

        last = change(last, F)

    if panel == 5:

        screen.fill(white)                                                      #background
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(student, (100,100))
        screen.blit(student, (450,100))
        screen.blit(student, (60,365))
        screen.blit(student, (500,365))
        screen.blit(sleeper, (190,355))
        screen.blit(student, (280,280))
        screen.blit(student, (380,215))
        screen.blit(student, (470,190))
        screen.blit(student, (220,185))
        screen.blit(student, (160,100))
        screen.blit(keener, (Xvals[num2], Yvals[num2]))

        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (190, 240) and mouse_y in range (355, 405):
            score += 1
            last = change(last, T)

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (Xvals[num2], Xvals[num2]+50) and mouse_y in range (Yvals[num2], Yvals[num2]+50):
            score -= 1
            last = change(last, T)

        pygame.display.flip()                                                   #displays screen and images

        last = change(last, F)

    if panel == 6:

        screen.fill(white)                                                      #background
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(student, (100,100))
        screen.blit(student, (450,100))
        screen.blit(student, (60,365))
        screen.blit(student, (500,365))
        screen.blit(student, (190,355))
        screen.blit(sleeper, (280,280))
        screen.blit(student, (380,215))
        screen.blit(student, (470,190))
        screen.blit(student, (220,185))
        screen.blit(student, (160,100))
        screen.blit(keener, (Xvals[num2], Yvals[num2]))

        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (280, 330) and mouse_y in range (280, 330):
            score += 1
            last = change(last, T)

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (Xvals[num2], Xvals[num2]+50) and mouse_y in range (Yvals[num2], Yvals[num2]+50):
            score -= 1
            last = change(last, T)

        pygame.display.flip()                                                   #displays screen and images

        last = change(last, F)

    if panel == 7:

        screen.fill(white)                                                      #background
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(student, (100,100))
        screen.blit(student, (450,100))
        screen.blit(student, (60,365))
        screen.blit(student, (500,365))
        screen.blit(student, (190,355))
        screen.blit(student, (280,280))
        screen.blit(sleeper, (380,215))
        screen.blit(student, (470,190))
        screen.blit(student, (220,185))
        screen.blit(student, (160,100))
        screen.blit(keener, (Xvals[num2], Yvals[num2]))

        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (380, 430) and mouse_y in range (215, 265):
            score += 1
            last = change(last, T)

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (Xvals[num2], Xvals[num2]+50) and mouse_y in range (Yvals[num2], Yvals[num2]+50):
            score -= 1
            last = change(last, T)

        pygame.display.flip()                                                   #displays screen and images

        last = change(last, F)

    if panel == 8:

        screen.fill(white)                                                      #background
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(student, (100,100))
        screen.blit(student, (450,100))
        screen.blit(student, (60,365))
        screen.blit(student, (500,365))
        screen.blit(student, (190,355))
        screen.blit(student, (280,280))
        screen.blit(student, (380,215))
        screen.blit(sleeper, (470,190))
        screen.blit(student, (220,185))
        screen.blit(student, (160,100))
        screen.blit(keener, (Xvals[num2], Yvals[num2]))

        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (470, 520) and mouse_y in range (190, 240):
            score += 1
            last = change(last, T)

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (Xvals[num2], Xvals[num2]+50) and mouse_y in range (Yvals[num2], Yvals[num2]+50):
            score -= 1
            last = change(last, T)

        pygame.display.flip()                                                   #displays screen and images

        last = change(last, F)

    if panel == 9:

        screen.fill(white)                                                      #background
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(student, (100,100))
        screen.blit(student, (450,100))
        screen.blit(student, (60,365))
        screen.blit(student, (500,365))
        screen.blit(student, (190,355))
        screen.blit(student, (280,280))
        screen.blit(student, (380,215))
        screen.blit(student, (470,190))
        screen.blit(sleeper, (220,185))
        screen.blit(student, (160,100))
        screen.blit(keener, (Xvals[num2], Yvals[num2]))

        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (220, 270) and mouse_y in range (185, 235):
            score += 1
            last = change(last, T)

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (Xvals[num2], Xvals[num2]+50) and mouse_y in range (Yvals[num2], Yvals[num2]+50):
            score -= 1
            last = change(last, T)

        pygame.display.flip()                                                   #displays screen and images

        last = change(last, F)

    if panel == 10:

        screen.fill(white)                                                      #background
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(student, (100,100))
        screen.blit(student, (450,100))
        screen.blit(student, (60,365))
        screen.blit(student, (500,365))
        screen.blit(student, (190,355))
        screen.blit(student, (280,280))
        screen.blit(student, (380,215))
        screen.blit(student, (470,190))
        screen.blit(student, (220,185))
        screen.blit(sleeper, (160,100))
        screen.blit(keener, (Xvals[num2], Yvals[num2]))

        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (160, 210) and mouse_y in range (100, 150):
            score += 1
            last = change(last, T)

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (Xvals[num2], Xvals[num2]+50) and mouse_y in range (Yvals[num2], Yvals[num2]+50):
            score -= 1
            last = change(last, T)

        pygame.display.flip()                                                   #displays screen and images

        last = change(last, F)

    if panel == 100:
        screen.fill(white)
        screen.blit(background, (0,0))                                         #changes background image
        screen.blit(student, (100,100))
        screen.blit(student, (450,100))
        screen.blit(student, (60,365))
        screen.blit(student, (500,365))
        screen.blit(student, (190,355))
        screen.blit(student, (280,280))
        screen.blit(student, (380,215))
        screen.blit(student, (470,190))
        screen.blit(student, (220,185))
        screen.blit(student, (160,100))
        screen.blit(Morgan, (208,140))



        screen.blit(Score, (50, 550))
        screen.blit(ScoreVal, (175, 550))
        screen.blit(Clock, (400, 550))
        screen.blit(ClockVal, (500, 550))
        pygame.display.flip()


#*************************************************************************************************************************************************#
#End stuff
clock.tick(60)                                                              #limits the game to 60 fps to keep speed constant







