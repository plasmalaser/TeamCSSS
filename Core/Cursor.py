
def DrawCursor(pygame, screen, Ghost, Gun):
    if pygame.mouse.get_pos()[0] < 1080 - 14:
        if Ghost:
            pygame.draw.circle(screen, (20, 22, 20), pygame.mouse.get_pos(), 14, 4)
            pygame.draw.circle(screen, (20, 22, 20), pygame.mouse.get_pos(), 7, 4)
        elif not Gun:
            pygame.draw.circle(screen, (22, 22, 204), pygame.mouse.get_pos(), 14, 4)
        elif Gun:
            pygame.draw.circle(screen, (204, 0, 0), pygame.mouse.get_pos(), 14, 4)
            pygame.draw.circle(screen, (204, 0, 0), pygame.mouse.get_pos(), 7, 4)
    elif pygame.mouse.get_pos()[0] > 1080 - 14 and pygame.mouse.get_pos()[0] < 1280 - 5:
        pygame.draw.circle(screen, (25,25,112), pygame.mouse.get_pos(), 5)

    return
