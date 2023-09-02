#Important note: After screen fill and before clock tick is where you render your game
#pygame.mouse.get_pressed() & pygame.mouse.get_pos() can be used to put the 'X' and 'O' on the board
#Call pygame.event.get() before the pygame.mouse.get_pressed() in order for it to work
#Need a "turn" variable to keep track of "x" and "o's" turn because I'm gonna put 1's in an array to 
#keep track of all the spots that are taken up. If a spot is taken up, then there will be a 1 in
#the correlated spot in an array. This will help me detect a win easier.
import pygame

screen_x = 450
screen_y = 450
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
running = True
turn = "X"
spots_array = [0,0,0,0,0,0,0,0,0]

#This function will return true or false for the LEFT mouse click
def get_mouse_click():
    pygame.event.get()
    click = pygame.mouse.get_pressed()
    return click[0]

def draw_middle_x():
    pygame.draw.line(screen, pygame.Color(255,165,0), (260, 150), (340, 210), width=2)
    pygame.draw.line(screen,pygame.Color(255,165,0),(260,210),(340,150), width=2)
    
def draw_board():
    #left
    pygame.draw.line(screen, pygame.Color(0,0,0), ((screen_x / 2) - 50, (screen_y * 0) + 100), ((screen_x / 2) - 50, screen_y - 100), width = 4)   
    #right
    pygame.draw.line(screen, pygame.Color(0,0,0), ((screen_x / 2) + 50, (screen_y * 0) + 100), ((screen_x / 2) + 50, screen_y - 100), width = 4)
    #top
    pygame.draw.line(screen, pygame.Color(0,0,0), ((screen_x * 0) + 100, (screen_y / 2) - 50), (screen_x - 100, (screen_y / 2) - 50), width = 4)   
    #bottom
    pygame.draw.line(screen, pygame.Color(0,0,0), ((screen_x * 0) + 100, (screen_y / 2) + 50), (screen_x - 100, (screen_y / 2) + 50), width = 4)    

pygame.init()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")

    draw_board() 
     
       
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()       