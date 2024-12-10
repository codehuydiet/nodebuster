import pygame
import sys
import time

# Cài đặt Pygame
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TEXT_COLOR = (0, 255, 0)

# Font
font = pygame.font.Font(None, 80) 
text = "NODEBUSTER" 
typing_speed = 0.05 

def typewriter_effect(text, font, color, x, y, screen, elapsed_time, speed):
    num_chars = min(len(text), int(elapsed_time / speed))
    displayed_text = text[:num_chars]
    displayed_text += "|" if int(elapsed_time * 2) % 2 == 0 else " "

    text_surface = font.render(displayed_text, True, color)
    screen.blit(text_surface, (x, y))
    return num_chars == len(text)

running = True
start_time = time.time()
finished_typing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed_time = time.time() - start_time

    screen.fill(BLACK)
    x, y = 100, HEIGHT // 2 - 50
    finished_typing = typewriter_effect(text, font, TEXT_COLOR, x, y, screen, elapsed_time, typing_speed)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
