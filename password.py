import pygame
import sys

class SecureTextInput:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the display
        self.screen = pygame.display.set_mode((960, 480))
        pygame.display.set_caption("Login")

        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Font
        self.font = pygame.font.Font(None, 36)

    # Secure text input function
    def text_input(self, prompt):
        text = ""
        input_rect = pygame.Rect(200, 200, 200, 50)
        active = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                elif event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            return text
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            self.screen.fill(self.WHITE)

            # Display asterisks instead of actual characters
            masked_text = '*' * len(text)
            text_surface = self.font.render(prompt + masked_text, True, self.BLACK)
            self.screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

            pygame.display.flip()
