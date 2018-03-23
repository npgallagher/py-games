# Imports
import pygame

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "MAZE"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
SILVER = (192, 192, 192)
GREEN = (0, 255, 0)

# Fonts
MY_FONT = pygame.font.Font(None, 50)
LEVEL_FONT = pygame.font.Font(None, 20)


# stages
START = 0
LEVEL1 = 1
LEVEL2 = 2
LEVEL3 = 3
LEVEL4 = 4
LEVEL5 = 5
LEVEL6 = 6
WIN = 7
LOSE = 8


#make bad block
#level4
bad_block1 = [200, 50, 50, 50]
bad_block2 = [50, 400, 100, 50]
bad_block3 = [600, 200, 100, 100]
bad_block4 = [400, 450, 50, 100]
bad_block5 = [300, 200, 50, 50]

#level 5
bad_block6 = [0, 250, 50, 100]
bad_block7 = [750, 250, 50, 100]
bad_block8 = [100, 250, 50, 100]
bad_block9 = [300, 250, 50, 100]
bad_block10 = [500, 250, 50, 100]



bad_blocks4 = [bad_block1, bad_block2, bad_block3, bad_block4, bad_block5]
bad_blocks5 = [bad_block6, bad_block7, bad_block8, bad_block9, bad_block10]

# make a wall
#level2
wall1 =  [300, 175, 200, 50]
wall2 =  [400, 450, 200, 50]
wall3 =  [100, 100, 50, 200]

#level3
wall4 = [300, 200, 150, 50]
wall5 = [300, 200, 50, 350]
wall6 = [450, 200, 50, 225]
wall7 = [300, 500, 350, 50]
wall8 = [450, 375, 200, 50]
wall9 = [650, 375, 50, 175]

#level5
wall10 = [0, 350, 350, 50]
wall11 = [450, 350, 350, 50]
wall12 = [300, 350, 50, 150]
wall13 = [450, 350, 50, 150]
wall14 = [300, 500, 200, 50]
wall15 = [0, 0, 800, 50]
wall16 = [0, 200, 350, 50]
wall17 = [450, 200, 350, 50]

#level6
wall18 = [0, 0, 25, 600]
wall19 = [0, 0, 800, 25]
wall20 = [775, 0, 25, 600]
wall21 = [0, 575, 375, 25]
wall22 = [425, 575, 375, 25]
wall23 = [25, 150, 75, 25]
wall24 = [25, 300, 75, 25]
wall25 = [75, 75, 100, 25]
wall26 = [150, 75, 25, 450]
wall27 = [75, 225, 75, 25]
wall28 = [75, 375, 25, 150]
wall29 = [100, 500, 50, 25]
wall30 = [225, 0, 25, 100]
wall31 = [175, 150, 150, 25]
wall32 = [300, 75, 25, 75]

walls2 = [wall1, wall2, wall3]
walls3 = [wall4, wall5, wall6, wall7, wall8, wall9]
walls5 = [wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17]
walls6 = [wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32]

#portal cores are squares in the portal (smaller than portal)
#teleport when intersects

#make portal cores
#level3
portal_core1 = [587, 452, 25, 25]


#make purple portals
#level3
purple_portal1 = [575, 440, 50, 50]

#make orange portals
#level3
orange_portal1 = [100, 100, 50, 50]

portal_cores3 = [portal_core1]
purple_portals3 = [purple_portal1]
orange_portals3 = [orange_portal1]


def setup():
    global block_pos, block_vel, size, speed
    
    block_pos = [375, 275]
    block_vel = [0, 0]
    size = 50
    speed = 5

def setup5():
    global block_pos5, block_vel5, size5, speed5

    block_pos5 = [390, 400]
    block_vel5 = [0, 0]
    size5 = 50
    speed5 = 5



def start():
    global stage

    stage = START


def rect_rect(w):
    left1 = block_pos[0]
    right1 = block_pos[0] + size
    top1 = block_pos[1]
    bottom1 = block_pos[1] + size
    
    left2 = w[0]
    right2 = w[0] + w[2]
    top2 = w[1]
    bottom2 = w[1] + w[3]


    return not (right1 <= left2 or
                right2 <= left1 or
                bottom1 <= top2 or
                bottom2 <= top1)

def rect_rect5(w):
    left1 = block_pos5[0]
    right1 = block_pos5[0] + size5
    top1 = block_pos5[1]
    bottom1 = block_pos5[1] + size5
    
    left2 = w[0]
    right2 = w[0] + w[2]
    top2 = w[1]
    bottom2 = w[1] + w[3]


    return not (right1 <= left2 or
                right2 <= left1 or
                bottom1 <= top2 or
                bottom2 <= top1)

# Game loop
setup()
start()
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = LEVEL1
                elif event.key == pygame.K_x:
                    pygame.quit()
                    
            elif stage == LEVEL1:
                if event.key == pygame.K_LEFT:
                    block_vel[0] = -1 * speed
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] = speed
                elif event.key == pygame.K_UP:
                    block_vel[1] = -1 * speed
                elif event.key == pygame.K_DOWN:
                    block_vel[1] = speed
                elif event.key == pygame.K_x:
                    pygame.quit()
                    
            elif stage == LEVEL2:
                if event.key == pygame.K_LEFT:
                    block_vel[0] = -1 * speed
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] = speed
                elif event.key == pygame.K_UP:
                    block_vel[1] = -1 * speed
                elif event.key == pygame.K_DOWN:
                    block_vel[1] = speed
                elif event.key == pygame.K_x:
                    pygame.quit()

            elif stage == LEVEL3:
                if event.key == pygame.K_LEFT:
                    block_vel[0] = -1 * speed
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] = speed
                elif event.key == pygame.K_UP:
                    block_vel[1] = -1 * speed
                elif event.key == pygame.K_DOWN:
                    block_vel[1] = speed
                elif event.key == pygame.K_x:
                    pygame.quit()
                    
            elif stage == LEVEL4:
                if event.key == pygame.K_LEFT:
                    block_vel[0] = -1 * speed
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] = speed
                elif event.key == pygame.K_UP:
                    block_vel[1] = -1 * speed
                elif event.key == pygame.K_DOWN:
                    block_vel[1] = speed
                elif event.key == pygame.K_x:
                    pygame.quit()

            elif stage == LEVEL5:
                if event.key == pygame.K_LEFT:
                    block_vel5[0] = -1 * speed
                elif event.key == pygame.K_RIGHT:
                    block_vel5[0] = speed
                elif event.key == pygame.K_UP:
                    block_vel5[1] = -1 * speed
                elif event.key == pygame.K_DOWN:
                    block_vel5[1] = speed
                elif event.key == pygame.K_x:
                    pygame.quit()

            elif stage == LEVEL6:
                if event.key == pygame.K_LEFT:
                    block_vel[0] = -1 * speed
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] = speed
                elif event.key == pygame.K_UP:
                    block_vel[1] = -1 * speed
                elif event.key == pygame.K_DOWN:
                    block_vel[1] = speed
                elif event.key == pygame.K_x:
                    pygame.quit()
                    
            elif stage == WIN:
                if event.key == pygame.K_SPACE:
                    setup()
                    start()
                elif event.key == pygame.K_x:
                    pygame.quit()

            elif stage == LOSE:
                if event.key == pygame.K_SPACE:
                    setup()
                    start()
                elif event.key == pygame.K_x:
                        pygame.quit()
                    
#change how velocity works        
        elif event.type == pygame.KEYUP:
            if stage == START:
                pass
            elif stage == LEVEL1:
                if event.key == pygame.K_LEFT:
                    block_vel[0] = 0
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] = 0
                elif event.key == pygame.K_UP:
                    block_vel[1] = 0
                elif event.key == pygame.K_DOWN:
                    block_vel[1] = 0
            elif stage == LEVEL2:
                if event.key == pygame.K_LEFT:
                    block_vel[0] = 0
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] = 0
                elif event.key == pygame.K_UP:
                    block_vel[1] = 0
                elif event.key == pygame.K_DOWN:
                    block_vel[1] = 0
            elif stage == LEVEL3:
                if event.key == pygame.K_LEFT:
                    block_vel[0] = 0
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] = 0
                elif event.key == pygame.K_UP:
                    block_vel[1] = 0
                elif event.key == pygame.K_DOWN:
                    block_vel[1] = 0
            elif stage == LEVEL4:
                if event.key == pygame.K_LEFT:
                    block_vel[0] = 0
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] = 0
                elif event.key == pygame.K_UP:
                    block_vel[1] = 0
                elif event.key == pygame.K_DOWN:
                    block_vel[1] = 0
            elif stage == LEVEL5:
                if event.key == pygame.K_LEFT:
                    block_vel5[0] = 0
                elif event.key == pygame.K_RIGHT:
                    block_vel5[0] = 0
                elif event.key == pygame.K_UP:
                    block_vel5[1] = 0
                elif event.key == pygame.K_DOWN:
                    block_vel5[1] = 0
            elif stage == LEVEL6:
                if event.key == pygame.K_LEFT:
                    block_vel[0] = 0
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] = 0
                elif event.key == pygame.K_UP:
                    block_vel[1] = 0
                elif event.key == pygame.K_DOWN:
                    block_vel[1] = 0
            elif stage == WIN:
                pass
            elif stage == LOSE:
                pass


    # Game logic
    if stage == LEVEL1:
        ''' move block '''
        block_pos[0] += block_vel[0]
        block_pos[1] += block_vel[1]

        ''' end game on wall collision '''
        if block_pos[0] < 0 or block_pos[0] > 750 or \
           block_pos[1] < 0 or block_pos[1] > 550:
            setup()
            stage = LEVEL2
            
    elif stage == LEVEL2:
        block = [block_pos[0], block_pos[1], (block_pos[0]+size), (block_pos[1]+size)]
        ''' move the block in horizontal direction '''
        block_pos[0] += block_vel[0]

        ''' resolve collisions '''
        for w in walls2:
            if rect_rect(w):        
                if block_vel[0]> 0:
                    block_pos[0] = w[0] - size
                elif block_vel[0] < 0:
                    block_pos[0] = w[0] + w[2]
        ''' move the block in vertical direction '''
        block_pos[1] += block_vel[1]
        
        ''' resolve collisions'''
        for w in walls2:
            if rect_rect(w):                    
                if block_vel[1] > 0:
                    block_pos[1] = w[1] - size
                if block_vel[1] < 0:
                    block_pos[1] = w[1] + w[3]

        ''' end game on wall collision '''
        if block_pos[0] < 0 or block_pos[0] > 750 or \
           block_pos[1] < 0 or block_pos[1] > 550:
            setup()
            stage = LEVEL3


    elif stage == LEVEL3:
        block = [block_pos[0], block_pos[1], (block_pos[0]+size), (block_pos[1]+size)]
        ''' move the block in horizontal direction '''
        block_pos[0] += block_vel[0]

        ''' resolve collisions '''
        for w in walls3:
            if rect_rect(w):        
                if block_vel[0]> 0:
                    block_pos[0] = w[0] - size
                elif block_vel[0] < 0:
                    block_pos[0] = w[0] + w[2]
        ''' move the block in vertical direction '''
        block_pos[1] += block_vel[1]
        
        ''' resolve collisions'''
        for w in walls3:
            if rect_rect(w):                    
                if block_vel[1] > 0:
                    block_pos[1] = w[1] - size
                if block_vel[1] < 0:
                    block_pos[1] = w[1] + w[3]
        for p in portal_cores3:
            if rect_rect(p):
                block_pos = [100, 100]

        ''' end game on wall collision '''
        if block_pos[0] < 0 or block_pos[0] > 750 or \
           block_pos[1] < 0 or block_pos[1] > 550:
            setup()
            stage = LEVEL4


    elif stage == LEVEL4:
        block = [block_pos[0], block_pos[1], (block_pos[0]+size), (block_pos[1]+size)]
        ''' move the block in horizontal direction '''
        block_pos[0] += block_vel[0]

        ''' resolve collisions '''
        

        for b in bad_blocks4:
            if rect_rect(b):
                stage = LOSE

        ''' move the block in vertical direction '''
        block_pos[1] += block_vel[1]

        for b in bad_blocks4:
            if rect_rect(b):
                stage = LOSE

        ''' end game on wall collision '''
        if block_pos[0] < 0 or block_pos[0] > 750 or \
            block_pos[1] < 0 or block_pos[1] > 550:
            setup5()
            stage = LEVEL5

    elif stage == LEVEL5:
        block = [block_pos5[0], block_pos5[1], (block_pos5[0]+size5), (block_pos5[1]+size5)]

        bad_block8[0] -= 5
        if bad_block8[0] <= 0:
            bad_block8[0] += 800
        bad_block9[0] -= 5
        if bad_block9[0] <= 0:
            bad_block9[0] += 800
        bad_block10[0] -= 5
        if bad_block10[0] <= 0:
            bad_block10[0] += 800

        
        ''' move the block in horizontal direction '''
        block_pos5[0] += block_vel5[0]

        for w in walls5:
            if rect_rect5(w):        
                if block_vel5[0]> 0:
                    block_pos5[0] = w[0] - size
                elif block_vel5[0] < 0:
                    block_pos5[0] = w[0] + w[2]

        for b in bad_blocks5:
            if rect_rect5(b):
                stage = LOSE

        ''' move the block in vertical direction '''
        block_pos5[1] += block_vel5[1]

        for w in walls5:
            if rect_rect5(w):                    
                if block_vel5[1] > 0:
                    block_pos5[1] = w[1] - size
                if block_vel5[1] < 0:
                    block_pos5[1] = w[1] + w[3]

        for b in bad_blocks5:
            if rect_rect5(b):
                stage = LOSE


        ''' end game on wall collision '''
        if block_pos5[0] < 0 or block_pos5[0] > 750 or \
            block_pos5[1] < 0 or block_pos5[1] > 550:
            setup()
            stage = LEVEL6

    elif stage == LEVEL6:
        block = [block_pos[0], block_pos[1], (block_pos[0]+size), (block_pos[1]+size)]
        ''' move the block in horizontal direction '''
        block_pos[0] += block_vel[0]

        ''' resolve collisions '''
        for w in walls6:
            if rect_rect(w):        
                if block_vel[0]> 0:
                    block_pos[0] = w[0] - size
                elif block_vel[0] < 0:
                    block_pos[0] = w[0] + w[2]

        #for b in bad_blocks6:
            #if rect_rect(b):
                #stage = LOSE

        ''' move the block in vertical direction '''
        block_pos[1] += block_vel[1]

        for w in walls6:
            if rect_rect(w):                    
                if block_vel[1] > 0:
                    block_pos[1] = w[1] - size
                if block_vel[1] < 0:
                    block_pos[1] = w[1] + w[3]

        #for b in bad_blocks6:
            #if rect_rect(b):
                #stage = LOSE

        ''' end game on wall collision '''
        if block_pos[0] < 0 or block_pos[0] > 750 or \
            block_pos[1] < 0 or block_pos[1] > 550:
            setup()
            stage = WIN

            
     
    # Drawing code
    
    if stage == START:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [block_pos[0], block_pos[1], size, size])
    elif stage == LEVEL1:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [block_pos[0], block_pos[1], size, size])
    elif stage == LEVEL2:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [block_pos[0], block_pos[1], size, size])
        for w in walls2:
            pygame.draw.rect(screen, RED, w)
    elif stage == LEVEL3:
        screen.fill(BLACK)
        for p in purple_portals3:
            pygame.draw.rect(screen, PURPLE, p)
        for o in orange_portals3:
            pygame.draw.rect(screen, ORANGE, o)
        pygame.draw.rect(screen, WHITE, [block_pos[0], block_pos[1], size, size])
        for w in walls3:
            pygame.draw.rect(screen, RED, w)
    elif stage == LEVEL4:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [block_pos[0], block_pos[1], size, size])
        for b in bad_blocks4:
            pygame.draw.rect(screen, GREEN, b)
    elif stage == LEVEL5:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [block_pos5[0], block_pos5[1], size5, size5])
        for b in bad_blocks5:
            pygame.draw.rect(screen, GREEN, b)
        for w in walls5:
            pygame.draw.rect(screen, RED, w)
    elif stage == LEVEL6:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [block_pos[0], block_pos[1], size, size])
        for w in walls6:
            pygame.draw.rect(screen, RED, w)
    elif stage == WIN:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [block_pos[0], block_pos[1], size, size])
    elif stage == LOSE:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [block_pos[0], block_pos[1], size, size])


    '''level counter'''
    if stage == START:
        pass
    elif stage == LEVEL1:
        level1 = LEVEL_FONT.render("1", True, WHITE)
        screen.blit(level1, [10, 10])
    elif stage == LEVEL2:
        level2 = LEVEL_FONT.render("2", True, WHITE)
        screen.blit(level2, [10, 10])
    elif stage == LEVEL3:
        level3 = LEVEL_FONT.render("3", True, WHITE)
        screen.blit(level3, [10, 10])
    elif stage == LEVEL4:
        level4 = LEVEL_FONT.render("4", True, WHITE)
        screen.blit(level4, [10, 10])
    elif stage == LEVEL5:
        level5 = LEVEL_FONT.render("5", True, WHITE)
        screen.blit(level5, [10, 10])
    elif stage == LEVEL6:
        level6 = LEVEL_FONT.render("6", True, WHITE)
        screen.blit(level6, [10, 10])


    ''' begin/end game text '''
    if stage == START:
        text1 = MY_FONT.render("Maze", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to play.)", True, WHITE)
        screen.blit(text1, [350, 150])
        screen.blit(text2, [225, 200])
    elif stage == WIN:
        text1 = MY_FONT.render("You Win", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])
    elif stage == LOSE:
        text1 = MY_FONT.render("You Lose", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window on quit
pygame.quit()
