''' faça um programa em pyton que abra e reproduza o áudo de um arquivo MP3'''

import pygame
pygame.init()
pygame.mixer.music.load('./exercicios/ex021a.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''from playsound import playsound
playsound('ex021.mp3')'''



