import pygame
import time
import random

pygame.init()


class item:
    # def __init__(self):

    def message(self, count, name, position, color):
        font = pygame.font.SysFont(None, 25)
        text = font.render( name + ": "+ str(count), True, color)
        gameDisplay.blit(text,(10,position))

    def things(self, filename ,thing_x, thing_y, thing_width):
        thing = pygame.transform.scale(pygame.image.load( filename + '.png'), (thing_width, thing_width))
        gameDisplay.blit(thing,(thing_x,thing_y))



#### screen_display
display_width = 800
display_height = 600


#### color
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
block_color = (53,115,255)
cyan = (0,255,255)

#### car argument
zombie_width = 110
face = 1


##### Lo
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('ZOMBIE_GAME')
clock = pygame.time.Clock()
zombie = pygame.transform.scale(pygame.image.load('zombie.png'), (110, 200))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def draw_zombie(x,y):
    gameDisplay.blit(zombie,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('LucidaBrightDemiBold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)


def game_over():

    for i in range(3,0,-1):
        die =  pygame.transform.scale(pygame.image.load("died.jpg"),(800,600))
        die.convert()
        gameDisplay.blit(die,(0,0))
        pygame.display.update()
        message_display(str(i))
    # message_display('You Died')

def main():

    ###### zombie_pos
    x = (display_width * 0.45)
    y = (display_height * 0.7)
    x_change = 0

    ###### money_argument
    money_startx = random.randrange(0, display_width)
    money_starty = -300
    money_width = 50
    money_height = 50

    ###### bloods_argument
    bloods_startx = random.randrange(0, display_width)
    bloods_starty = -300
    bloods_width = 70



    ###### thing var
    money_cnt = 0
    bloods = 3
    record = 1
    global face
    global zombie
    gameExit = False
    ######


    while not gameExit:

        ####### die
        if bloods <= 0:
             game_over()
             break
        ####### move
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    if (face == 2):
                        zombie = pygame.transform.flip(zombie, True, False)
                    face = 1
                    x_change = -20
                if event.key == pygame.K_RIGHT:
                    if (face == 1):
                        zombie = pygame.transform.flip(zombie, True, False)
                    face = 2
                    x_change = 20

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        ####### move_end



        # background
        image = pygame.image.load("background.jpg")
        image.convert()
        gameDisplay.blit(image, (0,0))


        ###### object
        blood = item()
        money = item()
        money.message(money_cnt,"Diamond",10,cyan)
        blood.message(bloods,"Blood",30,red)


        ####### check edge
        if (x + zombie_width) > display_width:
            x = display_width - zombie_width
            continue

        if (x <= 0):
            x = 1
            continue
        ####### check edge_end

        draw_zombie(x,y)

        ####### drop_it

        blood.things("Diamond_Sword",bloods_startx,bloods_starty,bloods_width)

        bloods_starty += 25

        if  bloods_starty > display_height:
            bloods_starty = 0 - bloods_starty
            bloods_startx = random.randrange(0,display_width)
            continue


        bloods_len = bloods_startx + bloods_startx + bloods_width

        if (y < bloods_starty + bloods_width):
            print('y crossover')
            if ( x <= (bloods_len) / 2 and (bloods_len) / 2 <= (x + zombie_width) ):
                bloods -= 1

                bloods_startx = random.randrange(0, display_width)
                bloods_starty = -300
                continue;

        ##############################################################
        money.things("Diamond",money_startx,money_starty,money_width)

        money_starty += 25

        if  money_starty > display_height:
            money_starty = 0 - money_starty
            money_startx = random.randrange(0,display_width)
            continue

        money_len = money_startx + money_startx + money_width

        if (y < money_starty + money_width):
            print('y crossover')
            if ( x <= (money_len) / 2 and (money_len) / 2 <= (x + zombie_width) ):
                money_cnt += 1

                money_startx = random.randrange(0, display_width)
                money_starty = -300
                continue;


        pygame.display.update()
        clock.tick(60)

        #### drop_it_end


if __name__ == "__main__":

    while True:
        main()
    pygame.quit()
    quit()