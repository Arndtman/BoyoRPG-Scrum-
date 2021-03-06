import pygame
import time
import random
import EnemyTest
import BossTest 
import BoyoRPG

homeTown = BoyoRPG.pygame.image.load('png/hometown.png')
house1 = BoyoRPG.pygame.image.load('png/house1.png')
house1Flip = pygame.transform.flip(house1, 1, 0)
house2 = BoyoRPG.pygame.image.load('png/house2.png')
path2 = BoyoRPG.pygame.image.load('png/path2.png')
path3 = BoyoRPG.pygame.image.load('png/path3.png') 
bridge3 = BoyoRPG.pygame.image.load('png/bridge3.png')
forest1 = BoyoRPG.pygame.image.load('png/ForestMap1-Magdaleno.png')
sunkenChapel = BoyoRPG.pygame.image.load('png/SunkenChapel.png')
cliff = BoyoRPG.pygame.image.load('png/cliff.png')
lavaLake = BoyoRPG.pygame.image.load('png/Lava_Lake_MapAM2.png')
lavaRoom = BoyoRPG.pygame.image.load('png/LavaRoom.png')
arena = BoyoRPG.pygame.image.load('png/arena.png') 


#AM 5/4/18: converted mapbools into string IDs
homeTownID = 'homeTown'
house1ID = 'house1'
house1FlipID = 'house1Flip'
house2ID = 'house2'
path2ID = 'path2'
path3ID = 'path3'
bridge3ID = 'bridge3'
forest1ID = 'forest'
sunkenChapelID = 'sunkenChapel'
cliffID = 'cliff'
lavaLakeID = 'lavaLake'
lavaRoomID = 'lavaRoom'
arenaID = 'arena'

arena1 = True
arena2 = False
arena3 = False
arena4 = False

currentMapID = homeTownID # DEFAULT


#THESE VALUES SHOULD PROBABLY NOT BE HERE FOR ANYTHING OTHER THAN TESTING
##display_width = 800
##display_height = 600 
blue = (0, 0, 255)
##green = (0, 200, 0)
##black = (0, 0, 0)
##gameDisplay = pygame.display.set_mode((display_width, display_height))


# creates a rect from given rectdata, sets event status
# then appends it to a given list
def addRectData2Rect(list, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    list.append(rect)
    
# creates a rect from given coords, (x0y0),(x1,y1), sets event status
# then appends it to a given list
def addCoords2Rect(list, xy1, xy2):
    rect = pygame.Rect(xy1[0], xy1[1], xy2[0] - xy1[0], xy2[1] - xy1[1])
    list.append(rect)




#BEGIN COLLISION RECT DICTIONARY LOADING
#AM 4/29/2018: implemented collisions dictionary
rectListDict = {}

#HOMETOWN
tempList = []
rectListDict[homeTownID] = tempList
#house1
addRectData2Rect(tempList, 105, 300, 120, 70)
addRectData2Rect(tempList, 110, 290, 110, 10)
addRectData2Rect(tempList, 120, 280, 90, 10)
addRectData2Rect(tempList, 130, 270, 70, 10)
addRectData2Rect(tempList, 140, 260, 50, 10)
addRectData2Rect(tempList, 145, 250, 35, 10)

#house1flip
addRectData2Rect(tempList, 515, 300, 120, 70)
addRectData2Rect(tempList, 520, 290, 110, 10)
addRectData2Rect(tempList, 530, 280, 90, 10)
addRectData2Rect(tempList, 540, 270, 70, 10)
addRectData2Rect(tempList, 550, 260, 50, 10)
addRectData2Rect(tempList, 555, 250, 35, 10)
addRectData2Rect(tempList, 560, 245, 20, 5)
#townhall
addRectData2Rect(tempList, 55, 5, 190, 210)
addRectData2Rect(tempList, 535, 5, 215, 215)
addRectData2Rect(tempList, 245, 5, 290, 135)

#HOUSE1FLIP
tempList = []
rectListDict[house1FlipID] = tempList
addRectData2Rect(tempList, 0, 0, 180, 270)
addRectData2Rect(tempList, 0, 200, 25, 600)
addRectData2Rect(tempList, 25, 350, 155, 170)
addRectData2Rect(tempList, 0, 570, 800, 30)
addRectData2Rect(tempList, 600, 435, 80, 110)
addRectData2Rect(tempList, 755, 0, 45, 600)
addRectData2Rect(tempList, 565, 35, 190, 65)
addRectData2Rect(tempList, 180, 30, 310, 70)
addRectData2Rect(tempList, 180, 95, 115, 30)
addRectData2Rect(tempList, 410, 100, 75, 30)
addRectData2Rect(tempList, 295, 240, 460, 195)
addRectData2Rect(tempList, 490, 5, 70, 210)

#HOUSE1
#Fixed infinite loop bug (appended and iterated forever)
#Still bugged, but only loops twice, too sick to care atm
tempList2 = []
print("minor logic bug in maplinks ln111")
for wallRect in tempList: # house1flip unflip
    print(wallRect.x) 
    addRectData2Rect(tempList2, 800 - wallRect.x - wallRect.w, wallRect.y, wallRect.w, wallRect.h)
rectListDict[house1ID] = tempList2
tempList2 = []

#Path2 BP Left then right tree cluster
tempList = []
rectListDict[path2ID] = tempList
addCoords2Rect(tempList, (0,0), (155,215))
addCoords2Rect(tempList, (160,0), (215,30))
addCoords2Rect(tempList, (160,40), (240,240))
#next trees clockwise from red square
addCoords2Rect(tempList, (530,80), (625,155))
addCoords2Rect(tempList, (620,65), (720,120))
addCoords2Rect(tempList, (665,120), (765,315))
addCoords2Rect(tempList, (560,120), (665,295))
addCoords2Rect(tempList, (530,150), (565,250))

#BRIDGE
tempList = []
rectListDict[bridge3ID] = tempList
addRectData2Rect(tempList, 275, 0, 230, 255)
addRectData2Rect(tempList, 270, 315, 235, 280)
addRectData2Rect(tempList, 520, 395, 210, 145)

#CLIFF BP from left to right (clockwise) across ladder and then counterclockwise
tempList = []
rectListDict[cliffID] = tempList
addCoords2Rect(tempList, (210,535), (245,600))
addCoords2Rect(tempList, (245,500), (305,545))
addCoords2Rect(tempList, (305,470), (340,520))
addCoords2Rect(tempList, (220,325), (340,465))
addCoords2Rect(tempList, (330,320), (375,370))
addCoords2Rect(tempList, (350,265), (410,315))
addCoords2Rect(tempList, (410,240), (445,290))
addCoords2Rect(tempList, (440,220), (610,270))
addCoords2Rect(tempList, (610,200), (655,245))
#ladder
addCoords2Rect(tempList, (685,200), (720,245))
addCoords2Rect(tempList, (725,220), (790,270))
addCoords2Rect(tempList, (790,245), (800,290))
#at 4 on cliff BP now
addCoords2Rect(tempList, (790,145), (800,195))
addCoords2Rect(tempList, (760,120), (790,170))
addCoords2Rect(tempList, (725,100), (760,145))
addCoords2Rect(tempList, (690,75), (725,120))
#cave entrance
addCoords2Rect(tempList, (620,50), (710,80))
addCoords2Rect(tempList, (610,75), (645,120))
addCoords2Rect(tempList, (575,100), (615,150))
addCoords2Rect(tempList, (510,130), (580,170))
addCoords2Rect(tempList, (470,150), (510,195))
addCoords2Rect(tempList, (410,170), (475,220))

#Lava Boss Room
tempList = []
rectListDict[lavaRoomID] = tempList
addRectData2Rect(tempList, 0, 0, 800, 160)

#Path3 BP
tempList = []
rectListDict[path3ID] = tempList
addCoords2Rect(tempList, (10,70), (100,170))
addCoords2Rect(tempList, (175,115), (265,225))
addCoords2Rect(tempList, (245,190), (345,285))
addCoords2Rect(tempList, (25,190), (180,290))
addCoords2Rect(tempList, (0,405), (285,525))

#House2 BP clockwise from spawn (door)
tempList = []
rectListDict[house2ID] = tempList
addCoords2Rect(tempList, (680,50), (785,460))
addCoords2Rect(tempList, (785,460), (800,600))
addCoords2Rect(tempList, (0,600), (800,600))
addCoords2Rect(tempList, (95,390), (125 ,425))
addCoords2Rect(tempList, (120,390), (230,450))
addCoords2Rect(tempList, (30,40), (225,390))
addCoords2Rect(tempList, (230,145), (335,215))
addCoords2Rect(tempList, (225,60), (680,180))
addCoords2Rect(tempList, (390,180), (520,240))
addCoords2Rect(tempList, (570,120), (680,215))
addCoords2Rect(tempList, (385,290), (520,460))
addCoords2Rect(tempList, (385,290), (520,460))

#END COLLISION RECT DICTIONARY LOADING


#Testing Mob
orc = pygame.image.load('png/orc.png')
orcRstride = pygame.image.load('png/enemyRstride.png')
orcRstride2 = pygame.image.load('png/enemyRstride2.png')
orcLstride = pygame.image.load('png/enemyLstride.png')
orcLstride2 = pygame.image.load('png/enemyLstride2.png')

#Boss Test
Boss1 = pygame.image.load('png/Boss1.png')
fball = pygame.image.load('png/fireball.png')
Rock = pygame.image.load('png/Rock.png')

Boss2A = pygame.image.load('png/Boss2A.png')
Boss2B = pygame.image.load('png/Boss2B.png')
Boss2C = pygame.image.load('png/Boss2C.png')
skull = pygame.image.load('png/skull1.png')



enemyList = list()

#AM 4/29/18: wrote boundary collision function
def checkMapCollisions(pInst, wInst, key):
    x = pInst.x + pInst.x_vel/2
    y = pInst.y + pInst.y_vel/2
    w = pInst.w
    h = pInst.h
    futurePlayRect = pygame.Rect(x, y, w, h)
    mapRectListDict = rectListDict[key]
    for collisionRect in mapRectListDict:
        pygame.draw.rect(BoyoRPG.gameDisplay, blue, collisionRect, 1)
        #the debug collision rects are not the same as the actual bounds
        #this is so to not confuse when visualizing rects
        x = collisionRect.x
        y = collisionRect.y
        w = collisionRect.w
        h = collisionRect.h - 1 - (pInst.h - 5)
        # rect bottom is shifted up pInst.h - 5 units in order to allow for clipping
        selectedRect = pygame.Rect(x, y, w, h)
        if futurePlayRect.colliderect(selectedRect):
            print("Collision at (",
                      pInst.x, " ,",
                      pInst.y,
                      ") going ",
                      pInst.x_vel, ", ",
                      pInst.y_vel)
            
            if pInst.x + pInst.w - 1 < selectedRect.left or pInst.x > selectedRect.right - 1 :
                pInst.x_vel = 0 #stop x velocity
            if pInst.y + pInst.h - 1 < selectedRect.top:
                pInst.y_vel = 0 #stop y velocity from the top
            if pInst.y - 1 > selectedRect.bottom - 1:
                pInst.y_vel = 0 #stop y velocity from the bottom
            """"print(" l:", selectedRect.left,
                      " r:", selectedRect.right,
                      " u:", selectedRect.top, 
                      " b:", selectedRect.bottom)
            """


def links(pInst, wInst, clk):
    global currentMapID
    global enemyList
    global arena1
    global arena2
    global arena3
    global arena4
    #print("current map is ", currentMapID)
    
    #click = BoyoRPG.pygame.mouse.get_pressed()
    click = []
    click.append(clk)
    
    currentMap = wInst.Map
    playRect = pygame.Rect(pInst.x, wInst.y, pInst.w, pInst.h)

#HOMETOWN
    if currentMapID is homeTownID:
        checkMapCollisions(pInst, wInst, homeTownID)
        if 340 + 100 >= pInst.x >= 340 and 588 + 35 >= pInst.y >= 588:
            wInst.Map = path2
            pInst.x = 555
            pInst.y = 25
            currentMapID = path2ID
        if 140 + 30 >= pInst.x >= 140 and 340 + 15 > pInst.y >= 340 and click[0] == 1:
            wInst.Map = house1
            pInst.x = 245
            pInst.y = 465
            pygame.mixer.music.load("wav/lullaby.wav")
            pygame.mixer.music.play(-1)
            currentMapID = house1ID
        if 550 + 30 >= pInst.x >= 550 and 335 + 15 > pInst.y >= 335 and click[0] == 1:
            wInst.Map = house1Flip
            pInst.x = 525
            pInst.y = 470
            pygame.mixer.music.load("wav/lullaby.wav")
            pygame.mixer.music.play(-1)
            currentMapID = house1FlipID
#HOUSE1
    if currentMapID is house1ID:
        checkMapCollisions(pInst, wInst, house1ID)
        if 225 + 60 >= pInst.x >= 225 and 402 + 15 > pInst.y >= 402 and click[0] == 1:
            wInst.Map = homeTown
            pInst.x = 190
            pInst.y = 360
            pygame.mixer.music.load("wav/MM.wav")
            pygame.mixer.music.play(-1)
            currentMapID = homeTownID
#HOUSE2         
    if currentMapID is house1FlipID:
        checkMapCollisions(pInst, wInst, house1FlipID)
        if 510 + 50 >= pInst.x >= 510 and 402 + 15 > pInst.y >= 402 and click[0] == 1:
            wInst.Map = homeTown
            pInst.x = 535
            pInst.y = 345
            pygame.mixer.music.load("wav/MM.wav")
            pygame.mixer.music.play(-1)
            currentMapID = homeTownID
#PATH2
    if currentMapID is path2ID:
        checkMapCollisions(pInst, wInst, path2ID)
        if 533 + 60 > pInst.x > 510 and 0 + 3 > pInst.y >= 0:
            wInst.Map = homeTown
            pInst.x = 380
            pInst.y = 555
            currentMapID = homeTownID
        if 0 + 12 > pInst.x >= 0 and 380 + 100 > pInst.y > 380:
            wInst.Map = bridge3
            pInst.x = 780
            pInst.y = 280
            currentMapID = bridge3ID
        if 420 + 80 > pInst.x > 420 and 588 + 12 >= pInst.y >= 588:
            wInst.Map = path3
            pInst.x = 170
            pInst.y = 15
            currentMapID = path3ID
#BRIDGE3
    if currentMapID is bridge3ID:
        checkMapCollisions(pInst, wInst, bridge3ID)
        if 780 + 20 > pInst.x > 780 and 240 + 60 > pInst.y > 240:
            wInst.Map = path2
            pInst.x = 15
            pInst.y = 430
            currentMapID = path2ID
        if 0 + 15 > pInst.x >= 0 and 290 + 80 > pInst.y > 290:
            wInst.Map = forest1
            pInst.x = 770
            pInst.y = 270
            pygame.mixer.music.load("wav/Life_in_forest.ogg")
            pygame.mixer.music.play(-1)
            currentMapID = forest1ID
        if 700 + 80 >= pInst.x >= 700 and 0 + 10>= pInst.y >= 0:
            wInst.Map = cliff
            pInst.x = 625
            pInst.y = 530
            pygame.mixer.music.load("wav/Great_pyramids.ogg")
            pygame.mixer.music.play(-1)
            currentMapID = cliffID
#CLIFF           
    if currentMapID is cliffID:
        checkMapCollisions(pInst, wInst, cliffID)
        if 500 + 260 >= pInst.x >= 500 and 580 + 20>= pInst.y >= 580:
            wInst.Map = bridge3
            pInst.x = 740
            pInst.y = 15
            pygame.mixer.music.load("wav/MM.wav")
            pygame.mixer.music.play(-1)
            currentMapID = bridge3ID
        if 640 + 35 >= pInst.x >= 635 and 70 + 20>= pInst.y >= 70:
            wInst.Map = lavaLake
            pInst.x = 765
            pInst.y = 480
            currentMapID = lavaLakeID
#LAVA CAVE
    if currentMapID is lavaLakeID:
        if 780 + 20 >= pInst.x >= 780 and 430 + 80>= pInst.y >= 430:
            wInst.Map = cliff
            pInst.x = 655
            pInst.y = 110
            currentMapID = cliffID
        if 10 + 20 >= pInst.x >= 10 and 325 + 35>= pInst.y >= 325:
            wInst.Map = lavaRoom
            pInst.x = 65
            pInst.y = 190
            pygame.mixer.music.load("wav/Battle_in_the_winter.ogg")
            pygame.mixer.music.play(-1)
            currentMapID = lavaRoomID

#LavaRoom (Boss) 
    if currentMapID is lavaRoomID:
        checkMapCollisions(pInst, wInst, lavaRoomID)
        if 5 + 15 >= pInst.x >= 5 and 150 + 30>= pInst.y >= 150:
            wInst.Map = lavaLake
            pInst.x = 65
            pInst.y = 360
            pygame.mixer.music.load("wav/Great_pyramids.ogg")
            pygame.mixer.music.play(-1)
            currentMapID = lavaLakeID

    
#FORREST            
    if currentMapID is forest1ID:
        if 780 + 20 > pInst.x > 780 and 255 + 50 > pInst.y > 255:
            wInst.Map = bridge3
            pInst.x = 15
            pInst.y = 315
            pygame.mixer.music.load("wav/MM.wav")
            pygame.mixer.music.play(-1)
            currentMapID = bridge3ID
#PATH3
    if currentMapID is path3ID:
        checkMapCollisions(pInst, wInst, path3ID)
        if 143 + 100 > pInst.x > 143 and 0 + 4 > pInst.y >= 0:
            wInst.Map = path2
            pInst.x = 450
            pInst.y = 580
            currentMapID = path2ID
        if 780 + 20 >= pInst.x >= 780 and 259 + 40>= pInst.y >= 259:
            wInst.Map = sunkenChapel
            pInst.x = 15 
            pInst.y = 105
            pygame.mixer.music.load("wav/Heroic Minor.ogg")
            pygame.mixer.music.play(-1)
            currentMapID = sunkenChapelID
        if 70 + 35 >= pInst.x >= 70 and 259 + 20>= pInst.y >= 259 and click[0] == 1:
            wInst.Map = house2
            pInst.x = 700
            pInst.y = 435
            pygame.mixer.music.load("wav/lullaby.wav")
            pygame.mixer.music.play(-1)
            currentMapID = house2ID
#HOUSE2
    if currentMapID is house2ID:
        checkMapCollisions(pInst, wInst, house2ID)
        if 712 + 70 >= pInst.x >= 712 and 407 + 70 > pInst.y >= 407 and click[0] == 1:
            wInst.Map = path3
            pInst.x = 90
            pInst.y = 300
            pygame.mixer.music.load("wav/MM.wav")
            pygame.mixer.music.play(-1)
            currentMapID = path3ID

#SUNKEN CHURCH
    if currentMapID is sunkenChapelID:
        if 0 + 12 >= pInst.x >= 0 and 90 + 60>= pInst.y >= 90:
            wInst.Map = path3
            pInst.x = 760
            pInst.y = 290
            pygame.mixer.music.load("wav/MM.wav")
            pygame.mixer.music.play(-1)
            currentMapID = path3ID
        if 620 + 40 >= pInst.x >= 620 and 35 + 65>= pInst.y >= 65:
            print("yep", pInst.x, pInst.y)
            wInst.Map = arena
            pInst.x = 60
            pInst.y = 70
            arena1 = True
            arena2 = False
            arena3 = False
            arena4 = False
            currentMapID = arenaID
            
    if currentMapID is arenaID:
        if 25 + 15 >= pInst.x >= 25 and 30 + 20>= pInst.y >= 20:
            print("yep2", pInst.x, pInst.y)
            wInst.Map = sunkenChapel
            pInst.x = 615
            pInst.y = 65  
            currentMapID = sunkenChapelID
             
            
    if wInst.Map != currentMap:
        setSpawnMap(wInst.Map)
        print ("Map Change: ", currentMapID)
        #if random.randint(0, 100) < 12:
            #BoyoRPG.loadScreen()


   # wInst.displayWorld()

   
def setSpawnMap(Map):
    global enemyList
    global arena1
    global arena2
    global arena3
    global arena4
    enemyList = list()

    if (Map == path2):
        e1 = EnemyTest.Mob(60, 300,BoyoRPG.orc)
        enemyList.append(e1)
        
        e1 = EnemyTest.Mob(60, 400,BoyoRPG.orc)
        enemyList.append(e1)
        
    elif (Map == path3):
        e1 = EnemyTest.Mob(560, 700,BoyoRPG.orc)
        enemyList.append(e1)
        
    elif (Map == bridge3):
        enemyList = [EnemyTest.Mob(60, 500,BoyoRPG.orc), EnemyTest.Mob(70,600,BoyoRPG.orc)]

    elif (Map == forest1):
        enemyList = [EnemyTest.Mob(60, 500,BoyoRPG.orc), EnemyTest.Mob(70,600,BoyoRPG.orc)]

    elif (Map == sunkenChapel):
        enemyList = [EnemyTest.Mob(60, 500,BoyoRPG.orc), EnemyTest.Mob(70,600,BoyoRPG.orc)]

#Special Boss Room
#Fireballs, Rocks, and Boss1 are loaded
    elif (Map == lavaRoom):
        B1 = BossTest.Boss(500, 100,Boss1)
        ball1 = BossTest.FireBall(B1.x - 20, B1.y - 20, fball)
        ball2 = BossTest.FireBall(B1.x - 20, B1.y + B1.h, fball)
        mylist2 = [B1, ball1, ball2]
        mylist = []
        for i in range(5):
            mylist.append(BossTest.Rocks(Rock))
        enemyList = mylist2 + mylist

    elif (Map == arena):
        mylist = []
        if arena1:
            mylist.append(BossTest.Boss2(500, 100, Boss2A))
            for i in range(2):
                mylist.append(EnemyTest.Mob(random.randint(50, 700),
                            random.randint(100, 600),BoyoRPG.orc))
            enemyList = mylist
            arena1 = False
            arena2 = True
        elif arena2:
            mylist.append(BossTest.Boss2(500, 100, Boss2B))
            for i in range(4):
                mylist.append(EnemyTest.Mob(random.randint(50, 700),
                            random.randint(100, 600),BoyoRPG.orc))
            mylist2 = []
            for i in range(5):
                mylist2.append(BossTest.Rocks(Rock))
            enemyList = mylist + mylist2
            arena2 = False
            arena3 = True
        elif arena3:
            B2 = BossTest.Boss(500, 100, Boss2C)
            skull1 = BossTest.FireBall(B2.x - 20, B2.y - 20, skull)
            skull2 = BossTest.FireBall(B2.x - 20, B2.y + B2.h, skull)
            mylist = [B2, skull1, skull2]
            for i in range(6):
                mylist.append(EnemyTest.Mob(random.randint(50, 700),
                            random.randint(100, 600),BoyoRPG.orc))
            mylist2 = [] 
            for i in range(4):                       
                mylist2.append(BossTest.Rocks(Rock))
            enemyList = mylist + mylist2
            BoyoRPG.growl.play()
            arena3 = False
            arena4 = True
        elif arena4:
            arena4 = False
                


def makeMobs(pInst, wInst):
    for x in range(0,len(enemyList)):
        #if not empty
        if enemyList[x]:
            enemyList[x].seek(pInst)
            enemyList[x].charCollision(pInst)
            
            if enemyList[x].health > 0:
                enemyList[x].displayMob()
                if type(enemyList[x]) is BossTest.Rocks and enemyList[0] is None:
                    enemyList[x] = None
                
            else:
                if type(enemyList[x]) is BossTest.FireBall:
                    enemyList[x].x = 1000
                    enemyList[x].y = -1000
                    if random.randint(0, 100) < 5 and enemyList[0] is not None:
                        enemyList[x].respawn(enemyList[0])
                else:
                    enemyList[x] = None

    if wInst.Map == arena:
        if all(v is None for v in enemyList):
            setSpawnMap(wInst.Map)
            
    #print(enemyList)


def clear():
    global currentMapID
    global enemyList
    pygame.mixer.music.load("wav/MM.wav")
    pygame.mixer.music.play(-1)
    enemyList = []
    currentMapID = homeTownID
    #SET DEFAULT TO HOMETOWN
