import pygame.mixer
import time

pygame.mixer.init(frequency=44100)
pygame.mixer.music.load("./2021-09-01_162607.mp3")
pygame.mixer.music.play(1)
time.sleep(10)
pygame.mixer.music.stop()