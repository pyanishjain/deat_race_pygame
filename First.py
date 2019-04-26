import pygame
import time
import random
pygame.init()

display_width = 900
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
block_color = (53,115,255)

car_width = 73

thingCount=1
dodged=0

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 55)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,[0,0])

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
    pygame.display.update()
    

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

    
def crash():
    global thingCount
    global dodged
    dodged=0
    thingCount=1
    
    message_display('You Crashed')
    
def Thing_Destroy():
    thing_starty=-10
    thing_speed=0
    
    
    


def game_loop():
    global dodged
    global thingCount

    x = (display_width * 0.45)
    y = (display_height*0.8689)

    x_change = 0
    gun_y_change=0
    
    thing_startx=random.randrange(50,display_width-30)
    thing_starty=100
    thing_speed=5
    thing_width=50
    thing_height=50
    
    gun_x=0
    gun_y=0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5        
                
                if event.key == pygame.K_RIGHT:
                    x_change = 5

                if event.key==pygame.K_UP:
                    gun_x=x+20
                    gun_y=y-6
                    gun_y_change=-10
                    print("Gun Is On Fire:")
                    
   

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
           
                
                    
        
        x += x_change
        gun_y+=gun_y_change
        
        gameDisplay.fill(white)
        
       
        pygame.draw.rect(gameDisplay,red,[gun_x,gun_y,20,20])

        #GUN DESTROY THE THING
        if gun_y< thing_starty+thing_height:
            if gun_x > thing_startx and gun_x < thing_startx + thing_width or gun_x+20 > thing_startx and gun_x + 20 < thing_startx+thing_width:
                print('gun destroy the object')
                dodged += 1
                thing_speed += 0.2
                thing_width += (dodged * 0.4)
                game_loop()
        
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

                
        
                
        #CAR CRASH WITH BOUNDARY 
        if x > display_width - car_width or x < 0:
            crash()
            
        #LOGIC FOR CRASH WITH THING    
        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
                
        if thing_starty > display_height:
            
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 0.2
            thing_width += (dodged * 0.4)
            
        
            
           
        

        
        
            
        things_dodged(dodged)    
        car(x,y)
        
        pygame.display.update()
        clock.tick(60)



game_loop()
pygame.quit()
quit()
