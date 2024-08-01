import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
ROOM_WIDTH, ROOM_HEIGHT = 100, 80
NUM_ROOMS = 15

# Define room types and colors
ROOM_TYPES = [
    ("Entrance Hall", (255, 0, 0)),  # Red
    ("Monster Lair", (0, 255, 0)),  # Green
    ("Treasure Chamber", (0, 0, 255)),  # Blue
    ("Trap Room", (255, 255, 0)),  # Yellow
    ("Puzzle Room", (255, 0, 255)),  # Magenta
    ("Hallway", (0, 255, 255)),  # Cyan
    ("Library", (192, 192, 192)),  # Light Gray
    ("Armory", (128, 128, 128)),  # Gray
    ("Secret Room", (255, 165, 0)),  # Orange
    ("Dining Hall", (0, 128, 0)),  # Dark Green
]

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Generator")


def generate_dungeon(num_rooms=NUM_ROOMS):
    return random.choices(ROOM_TYPES, k=num_rooms)


def draw_dungeon(dungeon):
    screen.fill((0, 0, 0))  # Clear the screen with black

    x, y = 50, 50  # Starting coordinates
    for index, (room_type, color) in enumerate(dungeon):
        pygame.draw.rect(screen, color, (x, y, ROOM_WIDTH, ROOM_HEIGHT))
        font = pygame.font.SysFont(None, 24)
        text = font.render(room_type, True, (255, 255, 255))
        screen.blit(text, (x + 5, y + 5))

        # Update position for next room
        x += ROOM_WIDTH + 10
        if x > WIDTH - ROOM_WIDTH:
            x = 50
            y += ROOM_HEIGHT + 10

    pygame.display.flip()


def main():
    dungeon = generate_dungeon(NUM_ROOMS)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_dungeon(dungeon)

    pygame.quit()


if __name__ == "__main__":
    main()
