import pygame
import sys
import pickle
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
GRAVITY = 0.8
JUMP_POWER = 18
PLAYER_SPEED = 6
PLATFORM_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (135, 206, 235)
PLAYER_COLOR = (255, 0, 0)
REWARD_COLOR = (255, 215, 0)
TEXT_COLOR = (255, 255, 255)
MENU_BG_COLOR = (25, 25, 112)
BUTTON_COLOR = (70, 70, 170)
BUTTON_HOVER_COLOR = (100, 100, 200)
LEVEL_COMPLETE_COLOR = (50, 200, 50)
EXIT_COLOR = (220, 20, 60)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)
title_font = pygame.font.SysFont(None, 72)
level_font = pygame.font.SysFont(None, 48)

class Button:
    def __init__(self, x, y, width, height, text, color=BUTTON_COLOR):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = BUTTON_HOVER_COLOR
        self.is_hovered = False

    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, TEXT_COLOR, self.rect, 2, border_radius=10)

        text_surf = font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        return self.is_hovered

    def is_clicked(self, mouse_pos, mouse_click):
        return self.rect.collidepoint(mouse_pos) and mouse_click

def save_game(game_state):
    try:
        with open('platformer_save.dat', 'wb') as file:
            pickle.dump(game_state, file)
        return True
    except:
        return False

def load_game():
    try:
        if os.path.exists('platformer_save.dat'):
            with open('platformer_save.dat', 'rb') as file:
                return pickle.load(file)
        return None
    except:
        return None

def show_menu():
    new_game_btn = Button(WIDTH//2 - 150, HEIGHT//2 - 50, 300, 60, "New Game")
    load_game_btn = Button(WIDTH//2 - 150, HEIGHT//2 + 30, 300, 60, "Load Game")
    exit_btn = Button(WIDTH//2 - 150, HEIGHT//2 + 110, 300, 60, "Exit", EXIT_COLOR)

    save_exists = os.path.exists('platformer_save.dat')

    menu_running = True
    while menu_running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_clicked = True

        screen.fill(MENU_BG_COLOR)

        title_text = title_font.render("Platformer Game", True, TEXT_COLOR)
        title_rect = title_text.get_rect(center=(WIDTH//2, HEIGHT//4))
        screen.blit(title_text, title_rect)

        new_game_btn.check_hover(mouse_pos)
        new_game_btn.draw(screen)

        load_game_btn.check_hover(mouse_pos)
        if not save_exists:
            disabled_text = font.render("No saved game found", True, (200, 200, 200))
            screen.blit(disabled_text, (WIDTH//2 - 125, HEIGHT//2 + 100))
        else:
            load_game_btn.draw(screen)

        exit_btn.check_hover(mouse_pos)
        exit_btn.draw(screen)

        if mouse_clicked:
            if new_game_btn.is_hovered:
                return "new"
            elif load_game_btn.is_hovered and save_exists:
                return "load"
            elif exit_btn.is_hovered:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

def get_level_design(level):
    if level == 1:
        platforms = [
            pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
            pygame.Rect(100, 450, 200, 20),
            pygame.Rect(400, 350, 200, 20),
            pygame.Rect(200, 250, 200, 20),
            pygame.Rect(500, 150, 200, 20),
        ]
        reward = pygame.Rect(600, 120, 30, 30)
        player_start = (100, 100)

    elif level == 2:
        platforms = [
            pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
            pygame.Rect(150, 500, 100, 20),
            pygame.Rect(350, 450, 100, 20),
            pygame.Rect(550, 400, 100, 20),
            pygame.Rect(350, 350, 100, 20),
            pygame.Rect(150, 300, 100, 20),
            pygame.Rect(350, 250, 100, 20),
            pygame.Rect(550, 200, 100, 20),
            pygame.Rect(350, 150, 100, 20),
        ]
        reward = pygame.Rect(350, 120, 30, 30)
        player_start = (100, 500)

    elif level == 3:
        platforms = [
            pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
            pygame.Rect(50, 500, 100, 20),
            pygame.Rect(250, 450, 100, 20),
            pygame.Rect(450, 400, 100, 20),
            pygame.Rect(650, 350, 100, 20),
            pygame.Rect(450, 300, 100, 20),
            pygame.Rect(250, 250, 100, 20),
            pygame.Rect(50, 200, 100, 20),
            pygame.Rect(250, 150, 100, 20),
            pygame.Rect(450, 100, 100, 20),
        ]
        reward = pygame.Rect(500, 70, 30, 30)
        player_start = (50, 470)

    else:  # Bonus level or levels > 3
        platforms = [
            pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
            pygame.Rect(WIDTH//2 - 300, 500, 600, 20),
            pygame.Rect(WIDTH//2 - 250, 400, 500, 20),
            pygame.Rect(WIDTH//2 - 200, 300, 400, 20),
            pygame.Rect(WIDTH//2 - 150, 200, 300, 20),
            pygame.Rect(WIDTH//2 - 100, 100, 200, 20),
        ]
        # Multiple rewards in the final level
        reward = [
            pygame.Rect(WIDTH//2 - 50, 70, 30, 30),
            pygame.Rect(WIDTH//2 + 50, 70, 30, 30)
        ]
        player_start = (WIDTH//2, 450)

    return platforms, reward, player_start

def show_level_complete(level, score):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    level_text = level_font.render(f"Level {level} Complete!", True, LEVEL_COMPLETE_COLOR)
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)

    level_rect = level_text.get_rect(center=(WIDTH//2, HEIGHT//3))
    score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//3 + 60))

    screen.blit(level_text, level_rect)
    screen.blit(score_text, score_rect)

    next_btn = Button(WIDTH//2 - 100, HEIGHT//2 + 50, 200, 50, "Next Level")

    pygame.display.flip()

    waiting = True
    while waiting:
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    waiting = False

        next_btn.check_hover(mouse_pos)
        next_btn.draw(screen)

        if mouse_clicked and next_btn.is_hovered:
            waiting = False

        pygame.display.flip()
        clock.tick(60)

def game_loop(loaded_state=None):
    if loaded_state:
        level = loaded_state.get('level', 1)
        player_x = loaded_state.get('player_x', 100)
        player_y = loaded_state.get('player_y', 100)
        score = loaded_state.get('score', 0)
        rewards_collected = loaded_state.get('rewards_collected', [])
    else:
        level = 1
        player_x, player_y = 100, 100
        score = 0
        rewards_collected = []

    while level <= 4:  # Max 4 levels including bonus level
        platforms, reward_data, (start_x, start_y) = get_level_design(level)

        if loaded_state and level == loaded_state.get('level', 1):
            player = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
        else:
            player = pygame.Rect(start_x, start_y, PLAYER_SIZE, PLAYER_SIZE)

        player_velocity_y = 0
        on_ground = False
        reward_message_timer = 0
        level_complete = False
        level_message_timer = 180  # Show level message for 3 seconds

        # For multi-reward levels
        if isinstance(reward_data, list):
            rewards = reward_data
            rewards_collected_this_level = [False] * len(rewards)
        else:
            rewards = [reward_data]
            rewards_collected_this_level = [False]

        pause_button = Button(WIDTH - 100, 20, 80, 40, "Menu")
        save_button = Button(WIDTH - 190, 20, 80, 40, "Save")

        running = True
        paused = False

        while running:
            mouse_pos = pygame.mouse.get_pos()
            mouse_clicked = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_state = {
                        'level': level,
                        'player_x': player.x,
                        'player_y': player.y,
                        'score': score,
                        'rewards_collected': rewards_collected
                    }
                    save_game(game_state)
                    return "exit"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and on_ground:
                        player_velocity_y = -JUMP_POWER
                    elif event.key == pygame.K_ESCAPE:
                        paused = not paused

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_clicked = True

            if not paused and not level_complete:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    player.x -= PLAYER_SPEED
                if keys[pygame.K_RIGHT]:
                    player.x += PLAYER_SPEED
                if keys[pygame.K_SPACE] and on_ground:
                    player_velocity_y = -JUMP_POWER
                    on_ground = False

                player_velocity_y += GRAVITY
                player.y += player_velocity_y

                if player.left < 0:
                    player.left = 0
                if player.right > WIDTH:
                    player.right = WIDTH

                on_ground = False

                for platform in platforms:
                    if player.colliderect(platform):
                        if player_velocity_y > 0 and player.bottom - player_velocity_y <= platform.top + 15:
                            player.bottom = platform.top
                            on_ground = True
                            player_velocity_y = 0
                        elif player_velocity_y < 0 and player.top - player_velocity_y >= platform.bottom - 15:
                            player.top = platform.bottom
                            player_velocity_y = 0.5
                        elif not on_ground:
                            if player.centerx < platform.centerx:
                                player.right = platform.left
                            else:
                                player.left = platform.right

                # Check for reward collection
                for i, reward in enumerate(rewards):
                    if not rewards_collected_this_level[i] and player.colliderect(reward):
                        rewards_collected_this_level[i] = True
                        score += 100 * level  # More points for higher levels
                        reward_message_timer = 120

                # Check if all rewards are collected to complete level
                if all(rewards_collected_this_level) and not level_complete:
                    level_complete = True
                    rewards_collected.append(level)

                if reward_message_timer > 0:
                    reward_message_timer -= 1

                if level_message_timer > 0:
                    level_message_timer -= 1

            screen.fill(BACKGROUND_COLOR)

            # Draw platforms
            for platform in platforms:
                pygame.draw.rect(screen, PLATFORM_COLOR, platform)

            # Draw rewards if not collected
            for i, reward in enumerate(rewards):
                if not rewards_collected_this_level[i]:
                    pygame.draw.rect(screen, REWARD_COLOR, reward)

            # Draw player
            pygame.draw.rect(screen, PLAYER_COLOR, player)

            # Draw score and level
            score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
            level_text = font.render(f"Level: {level}", True, TEXT_COLOR)
            screen.blit(score_text, (20, 20))
            screen.blit(level_text, (20, 60))

            # Show level notification at start
            if level_message_timer > 0:
                level_notif = level_font.render(f"Level {level}", True, TEXT_COLOR)
                level_rect = level_notif.get_rect(center=(WIDTH // 2, 100))
                screen.blit(level_notif, level_rect)

            # Show reward message
            if reward_message_timer > 0:
                message = f"REWARD COLLECTED! +{100 * level} POINTS!"
                message_text = font.render(message, True, REWARD_COLOR)
                text_rect = message_text.get_rect(center=(WIDTH // 2, 150))
                screen.blit(message_text, text_rect)

            # Draw menu and save buttons
            pause_button.check_hover(mouse_pos)
            pause_button.draw(screen)

            save_button.check_hover(mouse_pos)
            save_button.draw(screen)

            if mouse_clicked:
                if pause_button.is_hovered:
                    paused = True
                elif save_button.is_hovered:
                    game_state = {
                        'level': level,
                        'player_x': player.x,
                        'player_y': player.y,
                        'score': score,
                        'rewards_collected': rewards_collected
                    }
                    save_success = save_game(game_state)
                    save_msg = "Game Saved!" if save_success else "Save Failed!"
                    save_notification = font.render(save_msg, True, REWARD_COLOR)
                    screen.blit(save_notification, (WIDTH - 200, 70))
                    pygame.display.flip()
                    pygame.time.delay(1000)

            if level_complete:
                show_level_complete(level, score)
                level += 1
                break

            if paused:
                pause_overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                pause_overlay.fill((0, 0, 0, 128))
                screen.blit(pause_overlay, (0, 0))

                pause_text = level_font.render("PAUSED", True, TEXT_COLOR)
                pause_rect = pause_text.get_rect(center=(WIDTH//2, HEIGHT//4))
                screen.blit(pause_text, pause_rect)

                resume_btn = Button(WIDTH//2 - 100, HEIGHT//2 - 60, 200, 50, "Resume")
                save_btn = Button(WIDTH//2 - 100, HEIGHT//2, 200, 50, "Save Game")
                menu_btn = Button(WIDTH//2 - 100, HEIGHT//2 + 60, 200, 50, "Main Menu")

                resume_btn.check_hover(mouse_pos)
                resume_btn.draw(screen)

                save_btn.check_hover(mouse_pos)
                save_btn.draw(screen)

                menu_btn.check_hover(mouse_pos)
                menu_btn.draw(screen)

                if mouse_clicked:
                    if resume_btn.is_hovered:
                        paused = False
                    elif save_btn.is_hovered:
                        game_state = {
                            'level': level,
                            'player_x': player.x,
                            'player_y': player.y,
                            'score': score,
                            'rewards_collected': rewards_collected
                        }
                        save_success = save_game(game_state)
                        save_msg = "Game Saved!" if save_success else "Save Failed!"
                        save_notification = font.render(save_msg, True, REWARD_COLOR)
                        screen.blit(save_notification, (WIDTH//2 - 100, HEIGHT//2 + 120))
                        pygame.display.flip()
                        pygame.time.delay(1000)
                    elif menu_btn.is_hovered:
                        return "menu"

            pygame.display.flip()
            clock.tick(60)

    # After completing all levels
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    congrats_text = title_font.render("Congratulations!", True, LEVEL_COMPLETE_COLOR)
    finish_text = level_font.render("You completed all levels!", True, TEXT_COLOR)
    final_score = level_font.render(f"Final Score: {score}", True, REWARD_COLOR)

    congrats_rect = congrats_text.get_rect(center=(WIDTH//2, HEIGHT//3 - 50))
    finish_rect = finish_text.get_rect(center=(WIDTH//2, HEIGHT//3 + 20))
    score_rect = final_score.get_rect(center=(WIDTH//2, HEIGHT//3 + 80))

    screen.blit(congrats_text, congrats_rect)
    screen.blit(finish_text, finish_rect)
    screen.blit(final_score, score_rect)

    menu_btn = Button(WIDTH//2 - 100, HEIGHT//2 + 50, 200, 50, "Main Menu")
    exit_btn = Button(WIDTH//2 - 100, HEIGHT//2 + 120, 200, 50, "Exit Game", EXIT_COLOR)

    pygame.display.flip()

    waiting = True
    while waiting:
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_clicked = True

        menu_btn.check_hover(mouse_pos)
        menu_btn.draw(screen)

        exit_btn.check_hover(mouse_pos)
        exit_btn.draw(screen)

        if mouse_clicked:
            if menu_btn.is_hovered:
                return "menu"
            elif exit_btn.is_hovered:
                return "exit"

        pygame.display.flip()
        clock.tick(60)

    return "menu"

def main():
    action = "menu"

    while action != "exit":
        if action == "menu":
            action = show_menu()
        elif action == "new":
            action = game_loop()
        elif action == "load":
            loaded_state = load_game()
            if loaded_state:
                action = game_loop(loaded_state)
            else:
                action = "menu"

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
