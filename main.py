import pygame
from random import randint

def resize_image(image_path, new_width, new_height):
    image = pygame.image.load(image_path)
    resized_image = pygame.transform.scale(image, (new_width, new_height))
    pygame.image.save(resized_image, image_path)

def load_image(image_path):
    return pygame.image.load(image_path)

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

pygame.init()
directions = [randint(0, 1) for _ in range(15)]  
speeds_x = [randint(1, 5) for _ in range(15)]   
speeds_y = [randint(1, 6) for _ in range(15)]  
window = pygame.display.set_mode((1600, 800))
clock = pygame.time.Clock()
run = True

StonePNG = "Images/Stone.png"
PaperPNG = "Images/Paper.png"
ScissorsPNG = "Images/Scissors.png"

resize_image(StonePNG, 100, 100)
resize_image(PaperPNG, 100, 100)
resize_image(ScissorsPNG, 100, 100)

ShapeStone = load_image(StonePNG)
ShapePaper = load_image(PaperPNG)
ShapeScissors = load_image(ScissorsPNG)

StoneRect = ShapeStone.get_rect()
StoneRect.center = (800, 200)
StoneRect2 = ShapeStone.get_rect()
StoneRect2.center = (600, 200)
StoneRect3 = ShapeStone.get_rect()
StoneRect3.center = (700, 300)
StoneRect4 = ShapeStone.get_rect()
StoneRect4.center = (900, 300)
StoneRect5 = ShapeStone.get_rect()
StoneRect5.center = (800, 300)

PaperRect = ShapePaper.get_rect()
PaperRect.center = (200, 600)
PaperRect2 = ShapePaper.get_rect()
PaperRect2.center = (100, 600)
PaperRect3 = ShapePaper.get_rect()
PaperRect3.center = (300, 600)
PaperRect4 = ShapePaper.get_rect()
PaperRect4.center = (400, 700)
PaperRect5 = ShapePaper.get_rect()
PaperRect5.center = (500, 700)

ScissorsRect = ShapeScissors.get_rect()
ScissorsRect.center = (1500, 600)
ScissorsRect2 = ShapeScissors.get_rect()
ScissorsRect2.center = (1400, 600)
ScissorsRect3 = ShapeScissors.get_rect()
ScissorsRect3.center = (1300, 600)
ScissorsRect4 = ShapeScissors.get_rect()
ScissorsRect4.center = (1200, 700)
ScissorsRect5 = ShapeScissors.get_rect()
ScissorsRect5.center = (1100, 700)

shapes = [(ShapeStone,  StoneRect), (ShapePaper,  PaperRect), (ShapeScissors,  ScissorsRect),
          (ShapeStone, StoneRect2), (ShapePaper, PaperRect2), (ShapeScissors, ScissorsRect2),
          (ShapeStone, StoneRect3), (ShapePaper, PaperRect3), (ShapeScissors, ScissorsRect3),
          (ShapeStone, StoneRect4), (ShapePaper, PaperRect4), (ShapeScissors, ScissorsRect4),
          (ShapeStone, StoneRect5), (ShapePaper, PaperRect5), (ShapeScissors, ScissorsRect5)]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))

    for i, (shape, rect) in enumerate(shapes):
        if rect.left <= 0 or rect.right >= 1600:
            speeds_x[i] *= -1  
        if rect.top <= 0 or rect.bottom >= 800:
            speeds_y[i] *= -1  

        rect.move_ip(speeds_x[i], speeds_y[i])

        for j, (other_shape, other_rect) in enumerate(shapes):
            if i != j and check_collision(rect, other_rect):

                if (shape, other_shape) == (ShapeScissors, ShapePaper) or \
                   (shape, other_shape) == (ShapePaper, ShapeStone) or \
                   (shape, other_shape) == (ShapeStone, ShapeScissors):
                    shapes[i] = (other_shape, rect)
                    shapes[j] = (shape, other_rect)
                    

        window.blit(shape, rect)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
