import pygame
"""

"""
#Step1: Initialize Object
Obj = pygame.init()
#print(Obj)
#Step2: Creating a GUI Window
GameWindow = pygame.display.set_mode((400,400))
pygame.display.set_caption("My First Game Demo")
exit_Game == False

gameOver == False
#Step3: Naming your GUI
#Step4 : Infinite Loop
while not exit_Game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_Game = True
        if event.type == pygame.K_DOWN:
            if event.key == pygame.K_RIGHT:
                print("you have preessed Right arrow Kwy !!!! ")
            if event.key  == pygame.K_LEFT:
                print("yOU HAVE PRESSED lET ARROW EkEY ")
pygame.quit()
quit()
