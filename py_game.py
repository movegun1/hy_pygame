import pygame
import sys

pygame.init()

def 게임():
    print("게임이 실행되었습니다.")
    # 인게임 코드 붙여넣기
import pygame
import time
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 120
COLUMN_COUNT = 5
ROW_COUNT = 5
#마지막으로 클리어한 스테이지
last_cleared_stage = 0
#스테이지 변수 선언
current_stage = 1

# 각 스테이지별 시간 제한 (초 단위)
STAGE_TIME_LIMIT = 20# 테스트용
#STAGE_TIME_LIMIT = 80#찐
# 게임 시작 시간 초기화
start_time = time.time()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 이미지 로딩
off_image = pygame.image.load("0.png")
off_image = pygame.transform.scale(off_image, (CELL_SIZE, CELL_SIZE))
on_image = pygame.image.load("1.png")
on_image = pygame.transform.scale(on_image, (CELL_SIZE, CELL_SIZE))
clear_image = pygame.image.load("clear.png")  #
clear_image = pygame.transform.scale(clear_image, (CELL_SIZE, CELL_SIZE))  

#사운드로딩
background_sound = pygame.mixer.Sound("21463-HouseBed.wav")
background_sound.play(-1)
buttun_sound = pygame.mixer.Sound("Button.mp3")

GRAY = (180, 180, 180)
RED = (180, 180, 180)
SUCCESS_TEXT_COLOR = (0, 255, 0)  # 성공 텍스트의 색깔

# 각 셀의 상태를 저장
cell_states = [[True for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

# 버튼 눌림 효과를 위한 변수들
BUTTON_SCALE_NORMAL = 1.0  # 놓았을 때 버튼 크기
BUTTON_SCALE_PRESSED = 0.9  # 눌렸을 때 버튼 크기
is_button_pressed = False  # 버튼이 눌렸는지 여부를 나타내는 변수

def check_success():
    # 모든 셀이 빨간색이면 True, 그렇지 않으면 False 반환
    for row_index in range(ROW_COUNT):
        for column_index in range(COLUMN_COUNT):
            if not cell_states[row_index][column_index]:
                return False
    return True

def toggle_cells(row, column):
    # 십자가 모양
    cell_states[row][column] = not cell_states[row][column]  # 현재 셀
    if row > 0:
        cell_states[row - 1][column] = not cell_states[row - 1][column]  # 위쪽 셀
    if row < ROW_COUNT - 1:
        cell_states[row + 1][column] = not cell_states[row + 1][column]  # 아래쪽 셀
    if column > 0:
        cell_states[row][column - 1] = not cell_states[row][column - 1]  # 왼쪽 셀
    if column < COLUMN_COUNT - 1:
        cell_states[row][column + 1] = not cell_states[row][column + 1]  # 오른쪽 셀

#초기 상태
def initial_state():
    selected_cells = set()  # 중복되지 않는 선택된 셀을 저장하는 집합
    
    for i in range(5):
        while True:
            num1 = random.randint(0, 4)
            num2 = random.randint(0, 4)
            
            # 중복되지 않은 선택인 경우에만 집합에 추가
            if (num1, num2) not in selected_cells:
                selected_cells.add((num1, num2))
                toggle_cells(num1, num2)
                print(num1 + 1, num2 + 1)
                break

    print("=======")

# 스테이지 클리어 함수
def stage_clear():
    global current_stage,STAGE_TIME_LIMIT,last_cleared_stage
    screen.blit(clear_image, (250, 250))  # "clear.png" 이미지 표시
    # "clear.png" 이미지를 화면에 표시한 후 0.3초 동안 대기
    pygame.display.update()
    time.sleep(0.3)
    # 스테이지 증가
    current_stage += 1
    last_cleared_stage = current_stage
    STAGE_TIME_LIMIT += 10
    # 새로운 스테이지에 대한 초기화
    cell_states = [[True for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    initial_state()

# 게임 오버 함수
def game_over():
    screen.fill(RED)
    font = pygame.font.SysFont(None, 50)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    last_stage_text = font.render("Cleared Stage: {}".format(last_cleared_stage), True, (255, 255, 255))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    screen.blit(last_stage_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    exit()


#본 게임 함수
def game():
    initial_state()
    while True:
        screen.fill(GRAY)
        
        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = max(STAGE_TIME_LIMIT - elapsed_time, 0)  # 남은 시간 계산
        
        if remaining_time == 0:
            game_over()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                column_index = event.pos[0] // CELL_SIZE
                row_index = event.pos[1] // CELL_SIZE
                #효과음 출력
                buttun_sound.play()
                # 십자가 모양
                toggle_cells(row_index, column_index)
                
        for column_index in range(COLUMN_COUNT):
            for row_index in range(ROW_COUNT):
                cell_color = RED if cell_states[row_index][column_index] else GRAY
                cell_image = on_image if cell_states[row_index][column_index] else off_image
                pygame.draw.rect(screen, cell_color, pygame.Rect(column_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                if cell_image:
                    screen.blit(cell_image, (column_index * CELL_SIZE, row_index * CELL_SIZE))
        #스테이지 표시
        font = pygame.font.SysFont(None, 30)
        stage_text = font.render("Stage: " + str(current_stage), True, (255, 255, 255))
        screen.blit(stage_text, (10, 10))

        #시간표시
        font = pygame.font.SysFont(None, 30)
        time_text = font.render("Time: {:.1f}".format(remaining_time), True, (255, 255, 255))
        screen.blit(time_text, (10, 40))
    
        # 성공
        if check_success():
            # 스테이지 클리어 함수 호출
            stage_clear()
            
        pygame.display.update()
        clock.tick(30)
    
####

#여기에 메뉴 [시작하기]

#####




game()


if __name__ == "__main__":
    main()
