import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# --- Submarine box ---
sub_x = 300
sub_y = 200
sub_width = 600
sub_height = 240
sub_height += 20  # make taller from below
sub_radius = sub_height // 2

# --- Player setup ---
player_pos = pygame.Vector2(600, sub_y + sub_height // 2 + 75)
# Collision rect now covers arms, legs, and head
player_rect = pygame.Rect(player_pos.x - 35, player_pos.y - 20, 70, 70)  

def draw_doodle(screen, pos):
    x, y = int(pos.x), int(pos.y)
    # head
    pygame.draw.circle(screen, "white", (x, y - 20), 15, 3)
    # body
    pygame.draw.line(screen, "white", (x, y - 5), (x, y + 25), 3)
    # arms pointing down
    pygame.draw.line(screen, "white", (x, y + 5), (x - 20, y + 25), 3)
    pygame.draw.line(screen, "white", (x, y + 5), (x + 20, y + 25), 3)
    # legs
    pygame.draw.line(screen, "white", (x, y + 25), (x - 15, y + 50), 3)
    pygame.draw.line(screen, "white", (x, y + 25), (x + 15, y + 50), 3)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("darkblue")

    # --- Draw submarine ---
    pygame.draw.rect(screen, "grey", (sub_x + sub_radius, sub_y, sub_width - sub_height, sub_height))
    pygame.draw.circle(screen, "grey", (sub_x + sub_radius, sub_y + sub_radius), sub_radius)
    pygame.draw.circle(screen, "grey", (sub_x + sub_width - sub_radius, sub_y + sub_radius), sub_radius)
    # outline
    pygame.draw.rect(screen, "white", (sub_x + sub_radius, sub_y, sub_width - sub_height, sub_height), width=4)
    pygame.draw.circle(screen, "white", (sub_x + sub_radius, sub_y + sub_radius), sub_radius, width=4)
    pygame.draw.circle(screen, "white", (sub_x + sub_width - sub_radius, sub_y + sub_radius), sub_radius, width=4)

    # --- Player movement (horizontal only) ---
    keys = pygame.key.get_pressed()
    dx = 0
    speed = 300 * dt
    if keys[pygame.K_a]:
        dx = -speed
    if keys[pygame.K_d]:
        dx = speed

    new_rect = player_rect.move(dx, 0)

    # --- Horizontal collision (include arms) ---
    left_bound = sub_x + 20  # leave margin for left arm
    right_bound = sub_x + sub_width - 20  # leave margin for right arm
    if new_rect.left < left_bound:
        new_rect.left = left_bound
    if new_rect.right > right_bound:
        new_rect.right = right_bound

    player_rect = new_rect
    player_pos.x = player_rect.centerx

    # --- Draw player ---
    draw_doodle(screen, player_pos)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
