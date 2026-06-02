import os
import time
import platform
import cpuinfo 
import pygame
import sys
import random
pygame.init()
clock = pygame.time.Clock()
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),)
screen = pygame.display.set_mode((1280,720))
font = pygame.font.SysFont(None, 36)

input_rect = pygame.Rect(150, 200, 340, 40)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
box_color = color_inactive

pygame.display.set_caption("System Infomation")

cpu = cpuinfo.get_cpu_info()["brand_raw"]

os.system("clear")
if platform.system() == ("Linux"):
    if os.path.exists("/etc/debian_version"):
        msg4 = font.render("You are running on Debian Linux!", True, (0, 0, 0))
screen.fill("white")
msg1 = font.render(f"You are running {platform.system()}!", True, (0, 0, 0))
msg2 = font.render(f"Your CPU is the {cpu}", True, (0, 0 ,0))
msg3 = font.render("System Infomation Tool", True, (0, 0, 0))
screen.blit(msg1, (50, 120))
screen.blit(msg2, (50, 150))
screen.blit(msg3, (50, 30))


pygame.display.flip()
print(" ")
print(" ")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_u]:
            input_active = True
            text = ""
            if input_active:
                if event.type == pygame.TEXTINPUT:
                    text += event.text
            screen.fill(0)
            text_surf = font.render(text, True, (255, 255, 255 ))
            screen.blit(text_surf, (input_rect.x +5 , input_rect.y + 8))
            pygame.draw.rect(screen, box_color, input_rect, 2)
            pygame.display.flip()
            if platform.system() == ("Windows"):
                pkgtext = font.render("What package would you like to install? (Using WinGet): ", True, (0, 0, 0))
                screen.blit(pkgtext, (50, 200))
                pygame.display.flip()
            

        
