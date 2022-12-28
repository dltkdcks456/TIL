import pygame
from tkinter import *
import tkinter.messagebox
import random
import sys
from collections import deque
from pygame.locals import KEYDOWN, QUIT, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect, K_SPACE

pygame.init() # pygame 초기화
SURFACE = pygame.display.set_mode((400, 400))# 400 x 400 크기

# 일정 시간을 추적하는 데 사용할 수 있는 새 Clock 객체를 만든다.
# 시계는 게임의 프레임 속도를 제어하는 데 도움이 되는 몇 가지 기능을 제공
# clock.tick(60) -> 초당 60프레임
FPSCLOCK = pygame.time.Clock()

# pygame에서 전역변수 선언
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
isNeedToRestart = False

FOODS = []
SNAKE = deque()
(W, H) = (20, 20)

def init():
    global WHITE, BLACK, RED, GREEN, SURFACE, FPSCLOCK, FOODS, SNAKE, W, H
    pygame.init() # pygame 초기화
    SURFACE = pygame.display.set_mode((400, 400))# 400 x 400 크기

    # 일정 시간을 추적하는 데 사용할 수 있는 새 Clock 객체를 만든다.
    # 시계는 게임의 프레임 속도를 제어하는 데 도움이 되는 몇 가지 기능을 제공
    # clock.tick(60) -> 초당 60프레임
    FPSCLOCK = pygame.time.Clock()

    # pygame에서 전역변수 선언
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    FOODS = []
    SNAKE = deque()
    (W, H) = (20, 20)

def add_food():
    '''
    임의의 장소에 먹이 배치
    뱀과 먹이가 겹칠 경우 다른 곳에 배치 해야함.
    '''
    while True:
        pos = (random.randint(0, 19), random.randint(0, 19))
        # 뱀의 위치와 겹치면 다시 진행
        if pos in SNAKE and pos in FOODS:
            continue
        FOODS.append(pos)
        break

def move_food(pos):
    '''먹이를 다른 장소로 이동'''
    if len(FOODS) >=2 :
        i = FOODS.index(pos)
        del FOODS[i]
    add_food()

def paint():
    ''' 화면 전체 그리기 '''
    SURFACE.fill(WHITE)
    
    # 먹이 그리기
    for food in FOODS:
        pygame.draw.rect(SURFACE, RED, Rect(food[0] * 20, food[1] * 20, 20, 20))
    
    # 뱀 그리기
    idx = 0
    # 뱀의 길이에 따라 색깔 변경
    for body in SNAKE:
        if idx <= 4:
            pygame.draw.rect(SURFACE, GREEN, Rect(body[0] * 20, body[1] * 20, 20, 20))
        elif idx <= 9:
            pygame.draw.rect(SURFACE, (40, 240, 40), Rect(body[0] * 20, body[1] * 20, 20, 20))
        elif idx <= 14:
            pygame.draw.rect(SURFACE, (60, 240, 60), Rect(body[0] * 20, body[1] * 20, 20, 20))
        else:
            pygame.draw.rect(SURFACE, BLACK, Rect(body[0] * 20, body[1] * 20, 20, 20))
        idx += 1
    
    # 그리드 그리기
    for index in range(20):
        pygame.draw.line(SURFACE, BLACK, (index * 20, 0), (index * 20, 400))
        pygame.draw.line(SURFACE, BLACK, (0, index * 20), (400, index * 20))
    
    pygame.display.update()

def main():
    '''메인 함수'''
    # 초기 방향값 랜덤 추출
    key = random.choice([K_DOWN, K_UP, K_LEFT, K_RIGHT])
    
    
    # 게임 종료 신호
    game_over = False
    
    # 뱀 초기 위치 랜덤 설정
    SNAKE.append((random.randint(5, 15), random.randint(5, 15)))
    
    # 초기 먹이 설정
    add_food()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 스페이스 누르면 재시작
            elif event.type == KEYDOWN and key == K_SPACE:
                init()
                main()
            elif event.type == KEYDOWN:
                tmp = event.key
                if key == K_LEFT and tmp != K_RIGHT:
                    key = event.key
                elif key == K_RIGHT and tmp != K_LEFT:
                    key = event.key
                elif key == K_UP and tmp != K_DOWN:
                    key = event.key
                elif key == K_DOWN and tmp != K_UP:
                    key = event.key
            
        
        # 키보드 방향으로 움직임(단, 180도 회전은 못하게 만듦)
        if not game_over:
            if key == K_LEFT:
                head = (SNAKE[0][0] - 1, SNAKE[0][1])
            elif key == K_RIGHT:
                head = (SNAKE[0][0] + 1, SNAKE[0][1])
            elif key == K_UP:
                head = (SNAKE[0][0], SNAKE[0][1] - 1)
            elif key == K_DOWN:
                head = (SNAKE[0][0], SNAKE[0][1] + 1)
                
            # 뱀의 머리가 영역을 벗어나거나 자신의 몸체에 부딪힌다면 종료
            if head in SNAKE or head[0] < 0 or head[0] >= 20 or head[1] < 0 or head[1] >= 20:
                Tk().wm_withdraw()
                response = tkinter.messagebox.showinfo("", "게임 오버입니다.")

                if response == "ok":
                    init()
                    main()
                game_over = True
        
            # 뱀의 머리 이동
            SNAKE.appendleft(head)
            
            # 만약 먹이를 먹었을 경우 먹이 재생성
            if head in FOODS:
                # 뱀의 길이가 늘어남
                move_food(head)
            else:
                # 꼬리 자르기
                SNAKE.pop()
    
        paint()
        if len(SNAKE) < 5:
            FPSCLOCK.tick(5)
        elif len(SNAKE) <= 8:
            while len(FOODS) != 2:
                add_food()
            FPSCLOCK.tick(7)
        elif len(SNAKE) <= 12:
            while len(FOODS) != 3:
                add_food()
            FPSCLOCK.tick(10)
        else:
            FPSCLOCK.tick(13)
            


if __name__ == "__main__":
    main()