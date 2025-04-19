import pygame
import random
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎉 Happy Birthday Card 🎂")

# Colors
BABY_PINK = (255, 182, 193)  # baby pink background
PINK = (255, 182, 193)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)  # middle layer of the cake
PASTEL_PURPLE = (186, 85, 211)
YELLOW = (255, 255, 0)
BLUE = (135, 206, 250)
BLACK = (0, 0, 0)
CONFETTI_COLORS = [(255, 0, 0), (0, 255, 0), (0, 200, 255), (255, 255, 0), (255, 0, 255)]

# Fonts
font = pygame.font.SysFont("Comic Sans MS", 36)

# Confetti
confetti_active = False
confetti_particles = []

def draw_wishes():
    lines = [
        "Happy Birthday!",
        "Wishing you a loads of joy,",
        "laughter, and love ",
        "on your special day!",
    ]
    y = 50
    for line in lines:
        text = font.render(line, True, BLACK)
        screen.blit(text, (50, y))
        y += 50

def draw_cake():
    # Cake layers with updated colors
    pygame.draw.rect(screen, BROWN, (520, 260, 160, 50))   # bottom (brown)
    pygame.draw.rect(screen, WHITE, (540, 210, 120, 50))    # middle (white)
    pygame.draw.rect(screen, PASTEL_PURPLE, (560, 170, 80, 40))  # top (pastel purple)

    # Candles
    for x in [580, 600, 620]:
        pygame.draw.rect(screen, BLUE, (x, 150, 5, 20))
        pygame.draw.circle(screen, YELLOW, (x + 2, 145), 5)

def draw_confetti():
    global confetti_particles
    for i, (x, y, color, speed) in enumerate(confetti_particles):
        pygame.draw.circle(screen, color, (x, y), 4)
        confetti_particles[i] = (x, y + speed, color, speed)
    confetti_particles = [p for p in confetti_particles if p[1] < HEIGHT]

def generate_confetti():
    global confetti_particles
    for _ in range(100):
        x = random.randint(0, WIDTH)
        y = random.randint(-100, 0)
        color = random.choice(CONFETTI_COLORS)
        speed = random.randint(2, 6)
        confetti_particles.append((x, y, color, speed))

# Main loop
clock = pygame.time.Clock()
running = True

# Trigger confetti as soon as the card opens (game starts)
generate_confetti()
confetti_active = True

while running:
    screen.fill(BABY_PINK)  # Change background color to baby pink
    draw_wishes()
    draw_cake()
    if confetti_active:
        draw_confetti()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
