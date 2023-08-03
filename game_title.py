import pygame
import sys

pygame.init()

# 화면 크기
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# 색상
WHITE = (255, 255, 255)
BUTTON_COLOR1 = (100, 100, 100)
BUTTON_COLOR2 = (150, 150, 150)
BUTTON_COLOR3 = (200, 200, 200)

# 버튼 크기
BUTTON_WIDTH, BUTTON_HEIGHT = 600, 100

# 버튼 사이 간격
BUTTON_MARGIN = 10

# 폰트 파일
FONT_FILE = '경기천년제목_Medium.ttf'

# 초기화
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

# 버튼 생성 함수
def create_button(text, x, y, color):
    font = pygame.font.Font(FONT_FILE, 36)  # Change font size to 36
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    button_rect = pygame.Rect(x - BUTTON_WIDTH / 2, y - BUTTON_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    return text_surface, text_rect, button_rect, color

# 게임 함수
def 게임():
    print("게임이 실행되었습니다.")
    # 여기에 게임 로직을 추가하면 됩니다.

def main():
    # 타이틀 화면
    title_text = "Game Title"
    title_surface, title_rect, _, _ = create_button(title_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, (0, 0, 0))  # Change text color to black

    # 메뉴 화면
    button_x = SCREEN_WIDTH // 2
    button_y = SCREEN_HEIGHT // 2 + 150
    button1_text = "내 최고기록 표시"
    button1_surface, button1_rect, button1_rect_fill, button1_color = create_button(button1_text, button_x, button_y, BUTTON_COLOR2)
    button_y += BUTTON_HEIGHT + BUTTON_MARGIN
    button2_text = "내 도전 횟수"
    button2_surface, button2_rect, button2_rect_fill, button2_color = create_button(button2_text, button_x, button_y, BUTTON_COLOR3)
    button_y += BUTTON_HEIGHT + BUTTON_MARGIN
    button3_text = "내 최근 기록"
    button3_surface, button3_rect, button3_rect_fill, button3_color = create_button(button3_text, button_x, button_y, BUTTON_COLOR1)
    button_y += BUTTON_HEIGHT + BUTTON_MARGIN
    button4_text = "랭킹"
    button4_surface, button4_rect, button4_rect_fill, button4_color = create_button(button4_text, button_x, button_y, BUTTON_COLOR2)
    button_y += BUTTON_HEIGHT + BUTTON_MARGIN
    button5_text = "게임 시작"
    button5_surface, button5_rect, button5_rect_fill, button5_color = create_button(button5_text, button_x, button_y, BUTTON_COLOR3)

    show_title_screen = True
    show_menu_screen = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 아무 키나 누르면 타이틀 화면에서 메뉴 화면으로 전환
            if event.type == pygame.KEYDOWN and show_title_screen:
                show_title_screen = False
                show_menu_screen = True

            # 버튼 텍스트 누르면 해당 텍스트 표시
            if event.type == pygame.MOUSEBUTTONDOWN and show_menu_screen:
                mouse_pos = pygame.mouse.get_pos()
                if button1_rect.collidepoint(mouse_pos):
                    print(button1_text)
                elif button2_rect.collidepoint(mouse_pos):
                    print(button2_text)
                elif button3_rect.collidepoint(mouse_pos):
                    print(button3_text)
                elif button4_rect.collidepoint(mouse_pos):
                    print(button4_text)
                elif button5_rect.collidepoint(mouse_pos):
                    print(button5_text)
                    게임()

        if show_title_screen:
            screen.fill(WHITE)
            screen.blit(title_surface, title_rect)
        elif show_menu_screen:
            screen.fill(WHITE)
            pygame.draw.rect(screen, button1_color, button1_rect_fill, border_radius=15)
            screen.blit(button1_surface, button1_rect)
            pygame.draw.rect(screen, button2_color, button2_rect_fill, border_radius=15)
            screen.blit(button2_surface, button2_rect)
            pygame.draw.rect(screen, button3_color, button3_rect_fill, border_radius=15)
            screen.blit(button3_surface, button3_rect)
            pygame.draw.rect(screen, button4_color, button4_rect_fill, border_radius=15)
            screen.blit(button4_surface, button4_rect)
            pygame.draw.rect(screen, button5_color, button5_rect_fill, border_radius=15)
            screen.blit(button5_surface, button5_rect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
