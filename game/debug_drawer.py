"""

"""
import pygame
from . import settings

class DebugDrawer:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def draw_debug_elements(self, screen, current_time, active_enemies, last_enemy_release_time):
        center_x = settings.SCREEN_WIDTH // 2
        center_y = settings.SCREEN_HEIGHT // 2
        pygame.draw.line(
            screen,
            (settings.COLORS.get("WHITE")),
            (center_x, 0),
            (center_x, center_y),  # Adjust these coordinates accordingly
        )
        pygame.draw.line(
            screen,
            (settings.COLORS.get("BLUE")),
            (0, center_y),
            (settings.SCREEN_WIDTH, center_y),
        )
        pygame.draw.circle(
            screen,
            (settings.COLORS.get("PURPLE")),
            (center_x, center_y),  # Adjust these coordinates accordingly
            5,
            5,
            True,
            True,
            True,
            True,
        )

        time_text = self.font.render(f"Time: {current_time}", True, (255, 255, 255))
        active_enemies_text = self.font.render(
            f"Active enemies vs. All: {len(active_enemies)}/{len(pygame.sprite.Group.sprites(self.all_sprites))}",
            True,
            (255, 255, 255),
        )
        release_timer_text = self.font.render(
            f"Release timer: {current_time - last_enemy_release_time}",
            True,
            (255, 255, 255),
        )
        screen.blit(time_text, (10, 10))
        screen.blit(active_enemies_text, (10, 40))
        screen.blit(release_timer_text, (10, 70))
