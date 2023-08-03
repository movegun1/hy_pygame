import pygame
import firebase_admin
from firebase_admin import credentials, firestore
import requests

# Firebase 서비스 계정 키 경로
CREDENTIALS_PATH = "path/to/your/credentials.json"

# Firebase 초기화
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Firebase Firestore DB 초기화
db = firestore.client()

# 게임 제목과 화면 크기 설정
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Firebase Ranking")

# 색상 정의
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# 폰트 설정
pygame.font.init()
font = pygame.font.SysFont(None, 40)

# Firebase에서 랭킹 정보 가져오기
url = "https://your-firebase-project.firebaseio.com/ranking.json?orderBy=\"score\"&limitToLast=10"
response = requests.get(url)
ranking_data = response.json()

# 랭킹 정보를 리스트로 변환
ranking_list = [(name, score) for name, score in ranking_data.items()]

# 리스트를 점수 순으로 정렬
ranking_list.sort(key=lambda x: x[1], reverse=True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GRAY)

    # 랭킹 화면 출력
    rank_y = 50
    for i, (name, score) in enumerate(ranking_list[:10]):
        rank_text = font.render(f"{i+1}.", True, BLACK)
        name_text = font.render(name, True, BLACK)
        score_text = font.render(str(score), True, BLACK)

        screen.blit(rank_text, (100, rank_y))
        screen.blit(name_text, (150, rank_y))
        screen.blit(score_text, (500, rank_y))

        rank_y += 50

    pygame.display.flip()

pygame.quit()
