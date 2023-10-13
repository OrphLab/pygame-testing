import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
RECT_COLOR = (0, 0, 255)
RECT_SIZE = (100, 100)

# Create a Pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drag Rect with Right-Click")

# Create a Rect object to be dragged
draggable_rect = pygame.Rect(100, 100, *RECT_SIZE)
dragging = False  # Flag to track dragging state

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Right-click
            if draggable_rect.collidepoint(event.pos):
                dragging = True
                offset_x, offset_y = event.pos[0] - draggable_rect.x, event.pos[1] - draggable_rect.y
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            # Update the position of the draggable Rect while dragging
            draggable_rect.x, draggable_rect.y = event.pos[0] - offset_x, event.pos[1] - offset_y

    # Clear the screen
    window.fill(BACKGROUND_COLOR)

    # Draw the draggable Rect
    pygame.draw.rect(window, RECT_COLOR, draggable_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
