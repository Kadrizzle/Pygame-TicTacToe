#Important note: After screen fill and before clock tick is where you render your game
#pygame.mouse.get_pressed() & pygame.mouse.get_pos() can be used to put the 'X' and 'O' on the board
#Call pygame.event.get() before the pygame.mouse.get_pressed() in order for it to work

#After one of the if statements in the main loop I need to call a function that makes the computer play. 
#Once it plays I need to put a "1" in the "open_spots" array correlating with the spot the computer played

#When drawing X or O I need to keep track of the turns so I know which one to draw
import pygame

screen_x = 450
screen_y = 450
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
running = True
turn = "X"
spots_array = []
first_slot = pygame.draw.rect(screen, (255,255,255), (100, 99, 74, 74))
second_slot = pygame.draw.rect(screen, (255,255,255), (175, 99, 99, 74))
third_slot = pygame.draw.rect(screen, (255,255,255), (275, 99, 74, 74))
fourth_slot = pygame.draw.rect(screen, (255,255,255), (100, 174, 74, 99))
fifth_slot = pygame.draw.rect(screen, (255,255,255), (175, 174, 99, 99))
sixth_slot = pygame.draw.rect(screen, (255,255,255), (275, 174, 74, 99))
seventh_slot = pygame.draw.rect(screen, (255,255,255), (100, 274, 74, 74))
eigth_slot = pygame.draw.rect(screen, (255,255,255), (175, 274, 99, 74))
ninth_slot = pygame.draw.rect(screen, (255,255,255), (275, 274, 74, 74))
open_spots = [0, 0, 0, 0, 0, 0, 0, 0, 0]


#This function will return true or false for the LEFT mouse click
def get_mouse_click():
    pygame.event.get()
    click = pygame.mouse.get_pressed()
    return click[0]
    
    
def draw_board():
    #left line
    pygame.draw.line(screen, pygame.Color(0,0,0), ((screen_x / 2) - 45, (screen_y * 0) + 100), ((screen_x / 2) - 45, screen_y - 100), width = 6)   
    #right line
    pygame.draw.line(screen, pygame.Color(0,0,0), ((screen_x / 2) + 50, (screen_y * 0) + 100), ((screen_x / 2) + 50, screen_y - 100), width = 6)
    #top line
    pygame.draw.line(screen, pygame.Color(0,0,0), ((screen_x * 0) + 100, (screen_y / 2) - 47), (screen_x - 95, (screen_y / 2) - 47), width = 6)   
    #bottom line
    pygame.draw.line(screen, pygame.Color(0,0,0), ((screen_x * 0) + 100, (screen_y / 2) + 45), (screen_x - 95, (screen_y / 2) + 45), width = 6) 
    
#def computer_play():
    
   # for x in open_spots:
        
       
    
pygame.init()
screen.fill("white")
draw_board()


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                  
                   
    if get_mouse_click() == True:
        mouse_x, mouse_y = pygame.mouse.get_pos() 
        
        if first_slot.collidepoint(mouse_x, mouse_y) and open_spots[0] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (105, 105), (170, 170), width = 6)
            pygame.draw.line(screen, pygame.Color(64,61,88), (170, 105), (105, (screen_y /2) - 55), width = 6)
            open_spots[0] = 1
            
        if second_slot.collidepoint(mouse_x, mouse_y) and open_spots[1] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (195,105), (260, 170), width = 6)
            pygame.draw.line(screen, pygame.Color(64,61,88), (260, 105), (195, 170), width = 6) 
            open_spots[1] = 1
               
        if third_slot.collidepoint(mouse_x, mouse_y) and open_spots[2] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,105), (350,170), width = 6)
            pygame.draw.line(screen, pygame.Color(64,61,88), (285,170),(350,105), width = 6) 
            open_spots[2] = 1
                
        if fourth_slot.collidepoint(mouse_x, mouse_y) and open_spots[3] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (105,190), (170, 255), width = 6)
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (170,190), (105, 255), width = 6)
            open_spots[3] = 1
    
        if fifth_slot.collidepoint(mouse_x, mouse_y) and open_spots[4] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (195,190), (260, 255), width = 6)
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (260,190), (195, 255), width = 6)
            open_spots[4] = 1 
    
        if sixth_slot.collidepoint(mouse_x, mouse_y) and open_spots[5] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,190), (350,255), width = 6)
            pygame.draw.line(screen, pygame.Color(64,61,88), (285,255),(350,190), width = 6)
            open_spots[5] = 1
               
        if seventh_slot.collidepoint(mouse_x, mouse_y) and open_spots[6] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (105,280), (170, 345), width = 6)
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (170,280), (105, 345), width = 6)
            open_spots[6] = 1
            
        if eigth_slot.collidepoint(mouse_x, mouse_y) and open_spots[7] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (195,280), (260, 345), width = 6)
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (260,280), (195, 345), width = 6) 
            open_spots[7] = 1
            
        if ninth_slot.collidepoint(mouse_x, mouse_y) and open_spots[8] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,280), (350, 345), width = 6)
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,345), (350, 280), width = 6)
            open_spots[8] = 1
            
    # #first
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (105, 105), ((screen_x / 2) - 55, (screen_y / 2) - 55), width = 6)
    # pygame.draw.line(screen, pygame.Color(64,61,88), ((screen_x / 2) - 55, 105), (105, (screen_y /2) - 55), width = 6)
    # #second
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (195,105), (260, 170), width = 6)
    # pygame.draw.line(screen, pygame.Color(64,61,88), (260, 105), (195, 170), width = 6)
    # #fourth
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (105,190), (170, 255), width = 6)
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (170,190), (105, 255), width = 6)
    # #seventh
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (105,280), (170, 345), width = 6)
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (170,280), (105, 345), width = 6)
    # #fifth
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (195,190), (260, 255), width = 6)
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (260,190), (195, 255), width = 6)
    # #eighth
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (195,280), (260, 345), width = 6)
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (260,280), (195, 345), width = 6)
    # #third
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,105), (350,170), width = 6)
    # pygame.draw.line(screen, pygame.Color(64,61,88), (285,170),(350,105), width = 6)
    # #sixth
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,190), (350,255), width = 6)
    # pygame.draw.line(screen, pygame.Color(64,61,88), (285,255),(350,190), width = 6)   
    # #ninth
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,280), (350, 345), width = 6)
    # pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,345), (350, 280), width = 6) 
    
    
   
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()       
