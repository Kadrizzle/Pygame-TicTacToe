import pygame

pygame.init()
screen = pygame.display.set_mode((640,360))
clock = pygame.time.Clock()
running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")
    #Left line
    pygame.draw.line(screen, pygame.Color(0,0,0), (250, 60), (250, 300), width=4)
    #Right line
    pygame.draw.line(screen, pygame.Color(0,0,0), (350, 60), (350, 300), width=4)
    #Top line
    pygame.draw.line(screen, pygame.Color(0,0,0), (170, 140), (430, 140), width=4)
    #Bottom line
    pygame.draw.line(screen, pygame.Color(0,0,0), (170, 220), (430, 220), width=4)         
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()       
