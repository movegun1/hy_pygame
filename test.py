import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 정의
BLUE = (0, 150, 220)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)

# 결과 화면 요소 크기 설정
blue_rect_width, blue_rect_height = 600, 450
gray_rect_width, gray_rect_height = 450, 350
button_width, button_height = 180, 50

# 결과 화면 object 위치
blue_rect_x = (screen_width - blue_rect_width) // 2
blue_rect_y = (screen_height - blue_rect_height) // 2 - 25

gray_rect_x = (screen_width - gray_rect_width) // 2
gray_rect_y = (screen_height - gray_rect_height) // 2 - 50

button1_x = (screen_width - button_width * 2 - 20) // 2
button1_y = gray_rect_y + gray_rect_height + 20 - 10
button2_x = button1_x + button_width + 20
button2_y = gray_rect_y + gray_rect_height + 20 - 10

# 폰트 설정
font = pygame.font.Font('GGM.ttf', 20)
button_font = pygame.font.Font('GGM.ttf', 20)

# Pygame 창 제목 설정
pygame.display.set_caption("Game Result")

# 메인 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 배경 화면
    screen.fill(WHITE)

    # 파란색 직사각형
    pygame.draw.rect(screen, BLUE, (blue_rect_x, blue_rect_y, blue_rect_width, blue_rect_height), border_radius=10)

    # 회색 직사각형
    pygame.draw.rect(screen, GRAY, (gray_rect_x, gray_rect_y, gray_rect_width, gray_rect_height), border_radius=10)

    # 임시로 '임시1'과 같은 문자열로 처리, 나중에 변수 넣어서 사용
    ranking_text = font.render('Ranking: ' + '임시1', True, (255, 255, 255))
    score_text = font.render('Your Score: ' + '임시1', True, (255, 255, 255))
    ranking_rect = ranking_text.get_rect(center=(screen_width // 2, gray_rect_y + 100))
    score_rect = score_text.get_rect(center=(screen_width // 2, gray_rect_y + 150))
    screen.blit(ranking_text, ranking_rect)
    screen.blit(score_text, score_rect)

    # 버튼 그리기 (둥근 직사각형)
    pygame.draw.rect(screen, ORANGE, (button1_x, button1_y, button_width, button_height), border_radius=10)
    pygame.draw.rect(screen, ORANGE, (button2_x, button2_y, button_width, button_height), border_radius=10)

    # 버튼 텍스트 표시
    button1_text = button_font.render('다시하기', True, (255, 255, 255))
    button2_text = button_font.render('메인으로', True, (255, 255, 255))
    button1_rect = button1_text.get_rect(center=(button1_x + button_width // 2, button1_y + button_height // 2))
    button2_rect = button2_text.get_rect(center=(button2_x + button_width // 2, button2_y + button_height // 2))
    screen.blit(button1_text, button1_rect)
    screen.blit(button2_text, button2_rect)

    # 화면 업데이트
    pygame.display.flip()
