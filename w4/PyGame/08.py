import pygame
import time
import random

pygame.init()


#### screen_display
display_width = 800
display_height = 600


#### color
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
block_color = (53,115,255)

#### car argument
car_width = 110



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('RifleMan')
clock = pygame.time.Clock()

zombie = pygame.transform.scale(pygame.image.load('zombie.png'), (110, 200))


def message_garbage(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("killed: "+ str(count), True, black)
    gameDisplay.blit(text,(10,10))

def message_thing(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Money: "+ str(count), True, black)
    gameDisplay.blit(text,(10,30))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def garbage_things(sword_x,sword_y,sword_width):
    sword = pygame.transform.scale(pygame.image.load('Diamond_Sword.png'), (sword_width, sword_width))
    gameDisplay.blit(sword,(sword_x,sword_y))

def car(x,y):
    gameDisplay.blit(zombie,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('LucidaBrightDemiBold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)

    game_loop()



def crash():
    message_display('You Crashed')

def main():


    x = (display_width * 0.45)
    y = (display_height * 0.7)



    x_change = 0

    ###### random the thing
    thing_startx = random.randrange(0, display_width)
    thing_starty = -300
    thing_width = 50
    thing_height = 50

    ###### garbage the thing
    garbage_startx = random.randrange(0, display_width)
    garbage_starty = -300
    garbage_width = 70



    ###### thing var
    caught = 0
    garbage = 0
    record = 1
    gameExit = False
    ######


    while not gameExit:

        ####### move
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        message_garbage(garbage)
        message_thing(caught)
        ####### move_end

        ####### check edge
        if (x + car_width) > display_width:
            x = display_width - car_width
            continue

        if (x <= 0):
            x = 1
            continue
        ####### check edge_end
        car(x,y)





        #### drop_it
        if (record == 1):
            things(thing_startx, thing_starty, thing_width, thing_height, block_color)

            thing_starty += 10
            if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0,display_width)
                record = random.randint(1,2)
                continue

            thing_len = thing_startx + thing_startx + thing_width

            if (y < thing_starty + thing_height):
                print('y crossover')
                if ( x <= (thing_len) / 2 and (thing_len) / 2 <= (x + car_width) ):
                    caught += 1
                    thing_startx = random.randrange(0, display_width)
                    thing_starty = -300
                    continue;
        else :

            garbage_things(garbage_startx,garbage_starty,garbage_width)

            garbage_starty += 10
            if  garbage_starty > display_height:
                garbage_starty = 0 - garbage_starty
                garbage_startx = random.randrange(0,display_width)
                record = random.randint(1,2)
                continue


            garbage_len = garbage_startx + garbage_startx + garbage_width

            if (y < garbage_starty + garbage_width):
                print('y crossover')
                if ( x <= (garbage_len) / 2 and (garbage_len) / 2 <= (x + car_width) ):
                    garbage += 1
                    garbage_startx = random.randrange(0, display_width)
                    garbage_starty = -300
                    continue;


        pygame.display.update()
        clock.tick(60)
        #### drop_it_end


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()