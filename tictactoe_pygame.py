#Important note: After screen fill and before clock tick is where you render your game
#pygame.mouse.get_pressed() & pygame.mouse.get_pos() can be used to put the 'X' and 'O' on the board
#Call pygame.event.get() before the pygame.mouse.get_pressed() in order for it to work
#-------------------------------------------------------------------------------------------------------------------------
#After one of the if statements in the main loop I need to call a function that makes the computer play. 
#Once it plays I need to put a "1" in the "open_spots" array correlating with the spot the computer played
#----------------------------------------------------------------------------------------------------------------------------------------------
#Code below is how I'll be able to make a "computer_play" method. 
#Without the "circle_coordinates" array I more than likely won't be able to make a method for the computer
#pygame.draw.circle(screen, (240, 157, 81), circle_coordinates[0], (40), width = 6)

import random
import time
import pygame

screen_x = 450
screen_y = 450
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
running = True
turn = "X"
first_move = True
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
player_spots = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#Circle coordinates is necessary so I'll be able to have a method for the computer to play instead of manually writing down every move for the computer
#This will make more sense later when you actually go to type the method for the computer
circle_coordinates = [(135,135) , (228,135) , (320,135) , (135,225) , (228,225) , (320,225) , (135,315)  ,(228,315) , (320,315)]


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


#For the first move for the computer I'm gonna do a random value depending on the position that the player chooses    
def computer_play(open_spots, first_move):
    if first_move == True:
        for x in open_spots:
            rand_number = random.randint(0,8)
            if open_spots[rand_number] != 1:
                pygame.draw.circle(screen, pygame.Color(240,157,81), circle_coordinates[rand_number], (40), width = 6)
                open_spots[rand_number] = 1
                break
    else:
        first_number = 0
        second_number = 1
        for x in player_spots:
            if player_spots[first_number] == 1 and player_spots[second_number] == 1:
                pygame.draw.circle(screen, pygame.Color(240,157,81), circle_coordinates[second_number + 1], (40), width = 6)
                open_spots[second_number + 1] = 1
                if x == 2:
                    first_number = 0
                    second_number = 0
                first_number += 3 #0 = 3,4... 1 = 6,7... 2 = 9,10
                second_number += 3
                if x == 2:
                    first_number = 1
                    second_number = 2
                    if player_spots[first_number] == 1 and player_spots[second_number] == 1:
                        pygame.draw.circle(screen, pygame.Color(240,157,81), circle_coordinates[first_number - 1], (40), width = 6)
                        open_spots[first_number - 1] = 1
                        first_number += 3
                        second_number += 3
                        if x == 5: 
                            break
                
            
    
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
            player_spots[0] = 1
            computer_play(open_spots, first_move)
            first_move = False
            
        if second_slot.collidepoint(mouse_x, mouse_y) and open_spots[1] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (195,105), (260, 170), width = 6)
            pygame.draw.line(screen, pygame.Color(64,61,88), (260, 105), (195, 170), width = 6) 
            open_spots[1] = 1
            player_spots[1] = 1
            computer_play(open_spots, first_move)
            first_move = False
               
        if third_slot.collidepoint(mouse_x, mouse_y) and open_spots[2] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,105), (350,170), width = 6)
            pygame.draw.line(screen, pygame.Color(64,61,88), (285,170),(350,105), width = 6) 
            open_spots[2] = 1
            player_spots[2] = 1
            computer_play(open_spots, first_move)
            first_move = False
                
        if fourth_slot.collidepoint(mouse_x, mouse_y) and open_spots[3] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (105,190), (170, 255), width = 6)
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (170,190), (105, 255), width = 6)
            open_spots[3] = 1
            player_spots[3] = 1 
            computer_play(open_spots, first_move)
            first_move = False
    
        if fifth_slot.collidepoint(mouse_x, mouse_y) and open_spots[4] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (195,190), (260, 255), width = 6)
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (260,190), (195, 255), width = 6)
            open_spots[4] = 1
            player_spots[4] = 1
            computer_play(open_spots, first_move)
            first_move = False 
    
        if sixth_slot.collidepoint(mouse_x, mouse_y) and open_spots[5] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,190), (350,255), width = 6)
            pygame.draw.line(screen, pygame.Color(64,61,88), (285,255),(350,190), width = 6)
            open_spots[5] = 1
            player_spots[5] = 1
            computer_play(open_spots, first_move)
            first_move = False

        if seventh_slot.collidepoint(mouse_x, mouse_y) and open_spots[6] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (105,280), (170, 345), width = 6)
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (170,280), (105, 345), width = 6)
            open_spots[6] = 1
            player_spots[6] = 1
            computer_play(open_spots, first_move)
            first_move = False 

        if eigth_slot.collidepoint(mouse_x, mouse_y) and open_spots[7] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (195,280), (260, 345), width = 6)
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (260,280), (195, 345), width = 6) 
            open_spots[7] = 1
            player_spots[7] = 1
            computer_play(open_spots, first_move)
            first_move = False

        if ninth_slot.collidepoint(mouse_x, mouse_y) and open_spots[8] == 0:
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,280), (350, 345), width = 6)
            pygame.draw.line(screen, pygame.Color(64, 61, 88), (285,345), (350, 280), width = 6)
            open_spots[8] = 1
            player_spots[8] = 1
            computer_play(open_spots, first_move)
            first_move = False


    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()       