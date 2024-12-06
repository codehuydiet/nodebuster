"""loading"""

# import pygame
# import time

# # Khởi tạo pygame
# pygame.init()

# # Kích thước cửa sổ
# WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("Loading Screen Example")

# # Màu sắc
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)

# # Hàm hiển thị màn hình loading
# def show_loading_screen():
#     screen.fill(BLACK)
#     font = pygame.font.Font(None, 50)
#     text = font.render("Loading, please wait...", True, WHITE)
#     text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
#     screen.blit(text, text_rect)
#     pygame.display.flip()  # Hiển thị nội dung lên màn hình

# # Hàm tải dữ liệu
# def load_data():
#     total_steps = 10  # Tổng số bước tải
#     for step in range(total_steps):
#         # Giả lập thời gian tải dữ liệu (mỗi bước mất 0.5 giây)
#         time.sleep(0.5)
        
#         # Cập nhật thanh tiến trình
#         progress = (step + 1) / total_steps  # Tính phần trăm hoàn thành
#         update_loading_bar(progress)

# # Hàm cập nhật thanh tiến trình
# def update_loading_bar(progress):
#     bar_width = 400
#     bar_height = 30
#     bar_x = (WINDOW_WIDTH - bar_width) // 2
#     bar_y = (WINDOW_HEIGHT + 50) // 2

#     # Hiển thị nền
#     screen.fill(BLACK)

#     # Vẽ thanh nền
#     pygame.draw.rect(screen, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)

#     # Vẽ thanh tiến trình
#     pygame.draw.rect(screen, GREEN, (bar_x, bar_y, int(bar_width * progress), bar_height))

#     # Cập nhật màn hình
#     pygame.display.flip()

# # Main game loop
# def main_game():
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         screen.fill(WHITE)
#         font = pygame.font.Font(None, 50)
#         text = font.render("Main Game Screen", True, BLACK)
#         text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
#         screen.blit(text, text_rect)

#         pygame.display.flip()

# # Main program
# def main():
#     # Hiển thị màn hình loading
#     show_loading_screen()
    
#     # Tải dữ liệu
#     load_data()
    
#     # Chuyển sang màn hình chính
#     main_game()

# # Chạy chương trình
# if __name__ == "__main__":
#     main()

# pygame.quit()


"""test trong suot"""

# import pygame

# # Khởi tạo Pygame
# pygame.init()

# # Kích thước màn hình
# SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# clock = pygame.time.Clock()

# # Màu sắc
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# POPUP_COLOR = (200, 200, 200)

# # Kích thước pop-up
# POPUP_WIDTH, POPUP_HEIGHT = 200, 200
# POPUP_X = (SCREEN_WIDTH - POPUP_WIDTH) // 2
# POPUP_Y = (SCREEN_HEIGHT - POPUP_HEIGHT) // 2

# # Lớp phủ
# overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)  # Tạo surface trong suốt
# overlay.fill((255, 255, 255, 100))  # Màu đen với độ alpha 128 (50% trong suốt)

# # Vòng lặp chính
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Vẽ lớp phủ
#     screen.fill('black')  # Màu nền
#     screen.blit(overlay, (0, 0))  # Vẽ lớp phủ

#     # Vẽ pop-up
#     pygame.draw.rect(screen, POPUP_COLOR, (POPUP_X, POPUP_Y, POPUP_WIDTH, POPUP_HEIGHT))

#     # Vẽ nội dung trong pop-up (ví dụ: dòng chữ)
#     font = pygame.font.Font(None, 36)
#     text = font.render("This is a pop-up!", True, BLACK)
#     screen.blit(text, (POPUP_X + POPUP_WIDTH // 2 - text.get_width() // 2,
#                        POPUP_Y + POPUP_HEIGHT // 2 - text.get_height() // 2))

#     # Cập nhật màn hình
#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

"""test resize"""

import pygame
import sys
import ctypes
import os

pygame.init()

# Biến toàn cục lưu kích thước màn hình
SCREEN_SIZE = [800, 600]  # Mặc định là 800x600
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Resize Selector")

# Danh sách các kích thước có thể chọn
AVAILABLE_SIZES = [
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1920, 1080),
]

font = pygame.font.Font(None, 36)
selected_index = 0  # Chỉ số kích thước đang chọn


def center_window(screen_width, screen_height):
    user32 = ctypes.windll.user32
    screen_res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))  # Lấy độ phân giải màn hình
    pos_x = (screen_res[0] - screen_width) // 2
    pos_y = (screen_res[1] - screen_height) // 2
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{pos_x},{pos_y}"

def draw_selector(screen, selected_index):
    """Vẽ selector trên màn hình."""
    global AVAILABLE_SIZES

    # Vẽ nền selector
    selector_width = 300
    selector_height = len(AVAILABLE_SIZES) * 50 + 20
    selector_x = (SCREEN_SIZE[0] - selector_width) // 2
    selector_y = (SCREEN_SIZE[1] - selector_height) // 2

    # Vẽ nền selector
    pygame.draw.rect(screen, (50, 50, 50), (selector_x, selector_y, selector_width, selector_height))
    pygame.draw.rect(screen, (255, 255, 255), (selector_x, selector_y, selector_width, selector_height), 2)

    # Vẽ từng kích thước
    for i, size in enumerate(AVAILABLE_SIZES):
        color = (255, 255, 255) if i == selected_index else (150, 150, 150)
        size_text = font.render(f"{size[0]} x {size[1]}", True, color)
        text_x = selector_x + (selector_width - size_text.get_width()) // 2
        text_y = selector_y + 10 + i * 50
        screen.blit(size_text, (text_x, text_y))


def main():
    global SCREEN_SIZE, screen, selected_index

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Di chuyển lên trong selector
                    selected_index = (selected_index - 1) % len(AVAILABLE_SIZES)
                    center_window(SCREEN_SIZE[0], SCREEN_SIZE[1])
                elif event.key == pygame.K_DOWN:  # Di chuyển xuống trong selector
                    selected_index = (selected_index + 1) % len(AVAILABLE_SIZES)
                    center_window(SCREEN_SIZE[0], SCREEN_SIZE[1])
                elif event.key == pygame.K_RETURN:  # Nhấn Enter để chọn kích thước
                    SCREEN_SIZE = list(AVAILABLE_SIZES[selected_index])
                    print(SCREEN_SIZE)
                    center_window(SCREEN_SIZE[0], SCREEN_SIZE[1])
                    screen = pygame.display.set_mode(SCREEN_SIZE)
                    print(f"Screen size changed to: {screen}")
                    
        center_window(SCREEN_SIZE[0], SCREEN_SIZE[1])
        # Vẽ giao diện
        screen.fill((0, 0, 0))
        draw_selector(screen, selected_index)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
