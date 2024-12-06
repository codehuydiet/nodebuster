import pygame

class Selector:
    def __init__(self, x, y, width, height, options, font):
        self.rect = pygame.Rect(x, y, width, height)  # Vùng nút chính
        self.options = options  # Danh sách các tùy chọn
        self.current_index = 0  # Chỉ mục của tùy chọn hiện tại
        self.font = font
        self.is_open = False  # Trạng thái sổ xuống
        self.option_rects = [pygame.Rect(x, y + (i + 1) * height, width, height) for i in range(len(options))]  # Vùng các tùy chọn

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):  # Nhấp vào nút chính
                self.is_open = not self.is_open  # Đổi trạng thái sổ xuống
            elif self.is_open:
                for i, option_rect in enumerate(self.option_rects):  # Kiểm tra các tùy chọn
                    if option_rect.collidepoint(event.pos):
                        self.current_index = i  # Cập nhật tùy chọn hiện tại
                        self.is_open = False  # Đóng menu

    def draw(self, screen):
        # Vẽ nút chính
        pygame.draw.rect(screen, (200, 200, 200), self.rect)
        pygame.draw.rect(screen, (50, 50, 50), self.rect, 2)

        # Hiển thị tùy chọn hiện tại
        text_surface = self.font.render(self.options[self.current_index], True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        # Hiển thị các tùy chọn khi mở menu
        if self.is_open:
            for i, option_rect in enumerate(self.option_rects):
                pygame.draw.rect(screen, (200, 200, 200), option_rect)
                pygame.draw.rect(screen, (50, 50, 50), option_rect, 2)

                option_text = self.font.render(self.options[i], True, (0, 0, 0))
                option_text_rect = option_text.get_rect(center=option_rect.center)
                screen.blit(option_text, option_text_rect)

    def get_selected_option(self):
        return self.options[self.current_index]