import pygame
import random

# 初始化 Pygame
pygame.init()

# 設置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("馬力歐跳障礙物")

# 定義顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 定義遊戲中的角色和障礙物
mario_width = 50
mario_height = 60
mario_x = 50
mario_y = screen_height - mario_height
mario_y_change = 0
gravity = 0.6
jump_strength = -15

obstacle_width = 70
obstacle_height = 50
obstacle_speed = 7
obstacle_x = screen_width
obstacle_y = screen_height - obstacle_height

# 設置時鐘控制遊戲幀率
clock = pygame.time.Clock()
running = True

def draw_mario(x, y):
    pygame.draw.rect(screen, RED, [x, y, mario_width, mario_height])

def draw_obstacle(x, y):
    pygame.draw.rect(screen, BLACK, [x, y, obstacle_width, obstacle_height])

# 主遊戲循環
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and mario_y == screen_height - mario_height:
                mario_y_change = jump_strength

    # 更新馬力歐的位置
    mario_y_change += gravity
    mario_y += mario_y_change

    # 防止馬力歐掉出屏幕
    if mario_y > screen_height - mario_height:
        mario_y = screen_height - mario_height
        mario_y_change = 0

    # 更新障礙物的位置
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = screen_width + random.randint(0, 300)

    # 檢查碰撞
    if mario_x + mario_width > obstacle_x and mario_x < obstacle_x + obstacle_width:
        if mario_y + mario_height > obstacle_y:
            running = False

    # 填充屏幕背景
    screen.fill(WHITE)

    # 繪製馬力歐和障礙物
    draw_mario(mario_x, mario_y)
    draw_obstacle(obstacle_x, obstacle_y)

    # 更新屏幕
    pygame.display.flip()

    # 設置幀率
    clock.tick(60)

# 結束遊戲
pygame.quit()
