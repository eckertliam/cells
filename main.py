from cells import World, random_world
import pygame



pygame.init()
window = pygame.display.set_mode((500, 500))
world = random_world(500, 500)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)

    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size())//2]*2))

    pixel_array = pygame.PixelArray(window)
    
    world.update()
    
    world.render(pixel_array)

    pixel_array.close()
    
    pygame.display.flip()

pygame.quit()
exit()