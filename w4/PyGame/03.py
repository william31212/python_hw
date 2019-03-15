import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
gray = (100,100,100)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('zombie.png')
carImg = pygame.transform.scale(carImg, (50, 100))
carImg = pygame.transform.flip(carImg, True, False)


def car(x,y):
    gameDisplay.blit(carImg, (x,y))



x =  (display_width * 0.45)
y =  (display_height * 0.75)

car_speed = 0
record = 0

while not crashed:
    x_change = 0
    y_change = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if (record == 2):
                    carImg = pygame.transform.flip(carImg, True, False)
                record = 1
                x_change = -10
            elif event.key == pygame.K_RIGHT:
                if (record == 1):
                    carImg = pygame.transform.flip(carImg, True, False)
                record = 2
                x_change = 10
            elif event.key == pygame.K_UP:
                y_change = -10
            elif event.key == pygame.K_DOWN:
                y_change = 10

        if event.type == pygame.K_s:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

            carImg = pygame.transform.flip(carImg, True, False)

        ######################
    ##
    x += x_change
    y += y_change
    ##
    gameDisplay.fill(gray)
    car(x,y)

    pygame.display.update()
    clock.tick(1000)

pygame.quit()
quit()