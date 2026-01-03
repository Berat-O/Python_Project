import pygame


class Text:
    def __init__(self, window, text, font_size, color, alpha):
        self.window = window
        self.text = text
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.Font("Assets/BoldPixels.otf", self.font_size)
        self.text_surface = self.font.render(
            self.text, True, self.color
        ).convert_alpha()
        self.text_surface.set_alpha(alpha)
        self.alpha = alpha

    def draw(self, position):
        self.window.blit(self.text_surface, position)

    def update_text(self, new_text):
        self.text = new_text
        self.text_surface = self.font.render(
            self.text, True, self.color
        ).convert_alpha()
        self.text_surface.set_alpha(self.alpha)
