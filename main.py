import sys
import pygame
from game_of_life import GameofLife

pygame.init()
pygame.display.set_caption("Conway's Game of Life")

WIDTH = 700
HEIGHT = 700
SCALE = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

conway = GameofLife(screen, scale=SCALE, width=WIDTH, height=HEIGHT)

clock = pygame.time.Clock()
fps = 2

pause = False

while True:
    clock.tick(fps)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = not pause
                print("toggle")
            if event.key == pygame.K_k:
                conway.kill_all()
            if event.key == 61:
                fps+=1
                print("fps: " + str(fps))
            if event.key == pygame.K_MINUS:
                fps=fps - 1
                if fps <= 0:
                    fps = 1
                print("fps: " + str(fps))
            print(event.key)
            if event.key == pygame.K_g:
                print("Generation: " + str(conway.generation))
            if event.key == pygame.K_x:
                print(str(conway.row_to_hex(conway.grid[1].tolist())))
            if event.key == pygame.K_s:
                print("Step: ")
                print("  Generation: " + str(conway.generation))
                conway.run()


        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            cell = (int(pos[0]/SCALE), int(pos[1]/SCALE))
            print("Mouse Position: " + str(pos))
            print("Cell: " + str(cell))
            print("Grid State: " + str(conway.grid[cell[0], cell[1]]))
            conway.toggle_cell(cell[0], cell[1])

    if not pause:
        conway.run()
    pygame.display.update()
