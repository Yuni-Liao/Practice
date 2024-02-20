import sys
import pygame

pygame.init() # 初始化pygame
pygame.display.set_caption("來玩圈圈叉叉")

WIDTH = 600
HEIGHT = 600
GRID_SIZE = 200
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode([WIDTH, HEIGHT]) # 設定視窗大小

# 定義一個函數，用來畫圓圈或叉叉
def draw(screen, pos, circle=True):
    if circle:
        x = (GRID_SIZE // 2) + GRID_SIZE * pos[1]
        y = (GRID_SIZE // 2) + GRID_SIZE * pos[0]
        pygame.draw.circle(screen, YELLOW, [x, y], 70, width = 10)
    else:
        pygame.draw.line(
            screen,
            BLUE,
            [GRID_SIZE // 4 + GRID_SIZE * pos[1], GRID_SIZE // 4 + GRID_SIZE * pos[0]],
            [GRID_SIZE // 4 * 3 + GRID_SIZE * pos[1], GRID_SIZE // 4 * 3 + GRID_SIZE * pos[0]],
            width=8
        )
        
        pygame.draw.line(
            screen,
            BLUE,
            [GRID_SIZE // 4 * 3 + GRID_SIZE * pos[1], GRID_SIZE // 4 + GRID_SIZE * pos[0]],
            [GRID_SIZE // 4 + GRID_SIZE * pos[1], GRID_SIZE // 4 * 3 + GRID_SIZE * pos[0]],
            width=8
        )

# 這是畫格子的範例
pygame.draw.line(screen, RED, [GRID_SIZE, 0], [GRID_SIZE, HEIGHT], width=6)
pygame.draw.line(screen, RED, [0, GRID_SIZE], [WIDTH, GRID_SIZE], width=6)
pygame.draw.line(screen, RED, [0, GRID_SIZE * 2], [WIDTH, GRID_SIZE * 2], width=6)
pygame.draw.line(screen, RED, [GRID_SIZE * 2, 0], [GRID_SIZE * 2, HEIGHT], width=6) # width 是線的寬度

# 這是畫圓圈或叉叉的範例
# draw(screen, [0, 0])
# draw(screen, [2,2], circle=False)

# 這是畫圓圈
# pygame.draw.circle(screen, YELLOW, [100,100], 70, width = 10) #[0,0] 是圓心的位置, 70 是半徑
# pygame.draw.circle(screen, YELLOW, [100 + 1 * 200,100 + 2 * 200], 70, width = 10)
# pygame.draw.circle(screen, YELLOW, [100 + 2 * 200,100 + 1 * 200], 70, width = 10) 

# 這是畫叉叉
# pygame.draw.line(screen, BLUE, [GRID_SIZE // 4, GRID_SIZE // 4], [GRID_SIZE // 4 * 3, GRID_SIZE // 4 * 3], width=8)
# pygame.draw.line(screen, BLUE, [GRID_SIZE // 4 * 3, GRID_SIZE // 4], [GRID_SIZE // 4 , GRID_SIZE // 4 * 3], width=8)


pygame.display.flip() 


# 二維陣列 grid 用來記錄每個格子的狀態
# 0: 空格, 1: 圓圈, 2: 叉叉 
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

circle = True

while True:
    left, _, _ = pygame.mouse.get_pressed() # _ 是一個變數名稱，可以用來忽略不需要的變數

    if left:
        x, y = pygame.mouse.get_pos() # 取得滑鼠位置

        # 轉換座標
        pos_x = y // GRID_SIZE  
        pos_y = x // GRID_SIZE

        # 如果格子是空的，就畫圓圈或叉叉
        if not grid[pos_x][pos_y]:
            draw(screen, [pos_x, pos_y], circle)
            grid[pos_x][pos_y] = 1 if circle else 2 
            pygame.display.flip() 
            circle = False if circle else True # 輪到下一個玩家

    for event in pygame.event.get(): # 監聽事件
        if event.type == pygame.QUIT: sys.exit() # 退出事件

