import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the ball
ball_radius = 25
ball_x, ball_y = screen_width // 2, screen_height // 2
ball_speed = 20

# Main game loop
while True:
    screen.fill(WHITE)  # Fill the screen with white background

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle arrow key presses to move the ball
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - ball_speed, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + ball_speed, screen_height - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - ball_speed, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + ball_speed, screen_width - ball_radius)
