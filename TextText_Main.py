import pygame
pygame.init()



def draweverything(screen):
    pygame.display.flip()


if __name__ == "__main__":


    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("TextText")
    done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True