import pygame
import time

pygame.init()

WIDTH = 800
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

img1 = pygame.image.load("bdayimg1.jpg")
img2 = pygame.image.load("bdayimg2.jpg")
img3 = pygame.image.load("bdayimg3.jpg")
img4 = pygame.image.load("bdayimg4.jpg")
image1 = pygame.transform.scale(img1, (WIDTH, HEIGHT))
image2 = pygame.transform.scale(img2, (WIDTH, HEIGHT))
image3 = pygame.transform.scale(img3, (WIDTH, HEIGHT))
image4 = pygame.transform.scale(img4, (WIDTH, HEIGHT))

while (True):
    font1 = pygame.font.SysFont("Times New Roman", 72)
    text1 = font1.render("Happy", True, (0,0,0))
    text2 = font1.render("Birthday", True, (0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image1,(0,0))
    display_surface.blit(text1, (210,180))
    display_surface.blit(text2,(180,264))
    pygame.display.update()
    time.sleep(2)

    font2 = pygame.font.SysFont("Calibri", 72)
    text3 = font2.render("Happy", True, (0,0,0))
    text4 = font2.render("Birthday", True, (0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image2,(0,0))
    display_surface.blit(text3, (210,180))
    display_surface.blit(text4,(180,264))
    pygame.display.update()
    time.sleep(2)

    font3 = pygame.font.SysFont("Arial", 72)
    text5 = font3.render("Happy", True, (0,0,0))
    text6 = font3.render("Birthday", True, (0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image3,(0,0))
    display_surface.blit(text5, (210,180))
    display_surface.blit(text6,(180,264))
    pygame.display.update()
    time.sleep(2)

    font4 = pygame.font.SysFont("Comic Sans", 72)
    text7 = font4.render("Happy", True, (0,0,0))
    text8 = font4.render("Birthday", True, (0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image4,(0,0))
    display_surface.blit(text7, (210,180))
    display_surface.blit(text8,(180,264))
    pygame.display.update()
    time.sleep(2)

