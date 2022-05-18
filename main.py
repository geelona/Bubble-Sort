import sys
import pygame
import random
from elements import *
win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill(BLACK)

dr = True


def drawing():
    x = 0
    while x != WIDTH:
        r_num = random.randint(0, HEIGHT)
        nums_list.append(r_num)
        pygame.draw.line(win, WHITE, (x, HEIGHT), (x, HEIGHT - r_num))
        x += 1
        if x % 5 == 0:
            pygame.display.update()


def sort():
    for x in range(len(nums_list)):
        if x + 1 < WIDTH:
            if nums_list[x] > nums_list[x + 1]:
                trash = nums_list[x]
                nums_list[x] = nums_list[x + 1]
                nums_list[x + 1] = trash
            pygame.draw.line(win, BLACK, (x, HEIGHT), (x, 0))
            pygame.draw.line(win, WHITE, (x, HEIGHT), (x, HEIGHT - nums_list[x]))
            if x % (HEIGHT * 3) == 0:
                pygame.display.update()


def main():
    global dr
    clock = pygame.time.Clock()
    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if dr:
            dr = False
            drawing()
        else:
            sort()

        clock.tick(1000)


main()
