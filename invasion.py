# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random
import math

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "ALIEN INVASION"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
BLACK = (0, 0, 0)
RED = (242, 98, 31)
GREYBLUE = (190, 197, 209)
METAL = (104, 83, 83)
GREENGREY = (101, 124, 91)
GREY = (161, 165, 173)

  
def draw_saucer(x, y):
    pygame.draw.ellipse(screen, saucer, [x + 15, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, saucer, [x + 65, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREYBLUE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, saucer , [x + 30, y + 20, 60, 40])

def draw_ship(x, y):
    pygame.draw.rect(screen, GREYBLUE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, ship , [x + 30, y + 20, 60, 40])

def draw_smoke():
    for s in smoke:
        x = s
        y = (17 *(0-1) * (math.sqrt(x)) + 450) - 15
        # y = (math.sqrt(x) * 50) + 450
        pygame.draw.ellipse(screen, smokeo, [x, y, 25, 25])
        pygame.draw.ellipse(screen, smokeo, [x - 5, y, 30, 20])

    if s == 850:
        x = s[2]

def draw_meteor(x, y):
    pygame.draw.ellipse(screen, meteoro, [x, y + 5, 5 , 5])     


''' make saucers '''
saucers = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0 ,200)
    saucers.append([x, y])
''' make ships '''
ships = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0, 200)
    ships.append([x, y])

''' make meteor '''
meteor = []
for i in range(2000):
    x = random.randrange(0, 1500)
    y = random.randrange(-200,800)
    meteor.append([x, y])


smoke = []
for s in range(20):
    x = s * 50 + 310
    smoke.append(x)



    


# Game loop
        
done = False
ticks = 0
daytime = True
lights_on = False                              

                


while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_l:
                lights_on = not lights_on
   

    # Game logic
    ''' ticks '''
    frame = ticks // 5

    ticks += 1

    if ticks >= 40:
        ticks = 0
    ''' move saucers '''
    for c in saucers:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 200)
            
    ''' move ships '''
    for h in ships:
        h[0] -= 10

        if h[0] < -100:
            h[0] = random.randrange(800, 1600)
            h[1] = random.randrange(0, 200)


    ''' move meteor '''
    for m in meteor:
        m[1] += random.randint(2, 4) 
        m[0] -= random.randint(2, 3)

        if m[1] > 800:
            m[0] = random.randrange(000, 1500)
            m[1] = random.randrange(-200, 0)

    ''' set sky color '''
    if daytime:
        sky = RED
    else:
        sky = BLACK

    ''' set sun color '''
    if daytime:
        sun = YELLOW
    else:
        sun = WHITE
    ''' set saucer color '''
    if daytime:
        saucer = BLACK
    else:
        saucer = METAL

    ''' set ship color '''
    if daytime:
        ship = BLACK
    else:
        ship = METAL

    ''' set meteor color '''
    if daytime:
        meteoro = BLACK
    else:
        meteoro = RED
        
    ''' set smokeo color '''
    if daytime:
        smokeo = GREY
    else:
        smokeo = RED


    ''' set alien color '''
    if daytime:
        alien = RED
    else:
        alien = GREENGREY


    ''' set flyingsaucer color '''
    if daytime:
        flyingsaucer = BLACK
    else:
        flyingsaucer = METAL

    ''' set orb color '''
    if daytime:
        orb = GREYBLUE
    else:
        orb = RED
    # Drawing code
    ''' sky '''
    screen.fill(sky)

    ''' sun '''
    pygame.draw.ellipse(screen, sun, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 10):
        pygame.draw.polygon(screen, BLACK, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, BLACK, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, BLACK, [0, 410], [800, 410], 5)

    ''' alien '''
    pygame.draw.rect(screen, alien, [400, 200, 20, 75])
    pygame.draw.ellipse(screen, alien, [400, 150, 20, 50])
    pygame.draw.ellipse(screen, alien, [392, 150, 35, 35])
    pygame.draw.rect(screen, alien, [380, 200, 12, 50])
    pygame.draw.rect(screen, alien, [430, 200, 12, 50])
    pygame.draw.rect(screen, alien, [390, 200, 50, 10])
    pygame.draw.rect(screen, alien, [390, 275, 40, 10])
    pygame.draw.rect(screen, alien, [380, 275, 10, 50])
    pygame.draw.rect(screen, alien, [430, 275, 10, 50])
    pygame.draw.ellipse(screen, RED, [398, 160, 10, 20])
    pygame.draw.ellipse(screen, RED, [412, 160, 10, 20])
    ''' saucers '''
    for c in saucers:
        draw_saucer(c[0], c[1])



    ''' ships '''
    for h in ships:
        draw_ship(h[0], h[1])

    ''' meteor '''
    for m in meteor:
        draw_meteor(m[0], m[1])    

    smoke = [s + 1 if s < 800 else 310 for s in smoke]


    draw_smoke()


    ''' flying saucer '''
    pygame.draw.ellipse(screen, flyingsaucer, [265, 170, 50, 50])
    pygame.draw.ellipse(screen, flyingsaucer, [190, 170, 50, 50])
    pygame.draw.ellipse(screen, GREYBLUE, [230, 145, 50, 50])
    pygame.draw.rect(screen, flyingsaucer, [213, 170, 75, 50])
    pygame.draw.rect(screen, GREY, [290, 155, 10, 20])
    pygame.draw.ellipse(screen, orb, [205, 182, 20, 20])
    pygame.draw.ellipse(screen, orb, [280, 182, 20, 20])
    pygame.draw.ellipse(screen, orb, [243, 182, 20, 20])
    
        # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
