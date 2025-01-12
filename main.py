#!/usr/bin/env python3
import math
import random
import sys

import pygame


def get_rgb_color(color_str):
    if color_str == "white":
        return (255, 255, 255)
    elif color_str == "blue":
        return (0, 0, 255)
    elif color_str == "black":
        return (0, 0, 0)
    else:
        raise Exception("Unknown color!")


def play_game(screen, width, height):
    # Initialize variables used in game
    paddle_x = 100
    paddle_y = height // 2

    score = 0

    ball_x_speed = random.randint(2, 4)
    ball_y_speed = 2

    ball_x = width // 2
    ball_y = height // 2

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle_y -= 5
        elif keys[pygame.K_DOWN]:
            paddle_y += 5

        ball_x += ball_x_speed
        ball_y += ball_y_speed

        # Check for collisions
        # Right WALL
        if ball_x >= width - 10:
            ball_x_speed = -1 * ball_x_speed
        # Bottom WALL
        elif ball_y >= height - 10:
            ball_y_speed = -1 * ball_y_speed
        # Top WALL
        elif ball_y <= 10:
            ball_y_speed = -1 * ball_y_speed
        # Player missed
        elif ball_x <= -30:
            pygame.quit()
            sys.exit()
        # Collision when ball hits the paddle
        elif (
            ball_x <= paddle_x + 30 and ball_x >= paddle_x - 30 and ball_y >= paddle_y - 50 and ball_y <= paddle_y + 50
        ):
            ball_x_speed = -1 * ball_x_speed
            ball_y_speed = -1 * ball_y_speed
            score += 1

        # Draw paddles/ball in proper position
        screen.fill(get_rgb_color("black"))
        pygame.draw.rect(screen, (255, 255, 255), (paddle_x, paddle_y, 20, 80))
        pygame.draw.circle(screen, (0, 0, 255), (ball_x, ball_y), 10)
        # ------------------------------------------------------------
        # Set score font
        font = pygame.font.Font(None, 48)
        text_color = (255, 255, 255)
        text_surface = font.render(f"Score: {score}", True, text_color)

        # Position the text at the center of the screen
        text_rect = text_surface.get_rect(center=(700, 550))

        # Draw the text to the screen
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        # ------------------------------------------------------------


# Main "hook"
if __name__ == "__main__":
    print("Welcome to pong!!! Let's get started!")
    pygame.init()

    # Set up the game window
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")

    play_game(screen, width, height)
