import pygame
from pygame import mixer
import os

pygame.init()
mixer.init()
icon=pygame.image.load(r"playlist/uret1.jpg")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((580, 580))
pygame.display.set_caption("Playlist Music")
clock = pygame.time.Clock()
fps = 24

background = pygame.image.load("playlist/aya.jpg")


play_button = pygame.image.load("playlist/buttonplay.png")
pause_button = pygame.image.load("playlist/buttonpause.png")
next_button = pygame.image.load("playlist/buttonnext.png")
prev_button = pygame.image.load("playlist/buttonprevious.png")

music_directory = "C:/Users/Ausu/Documents/GitHub/Lab-7/musics"
playlist = [os.path.join(music_directory, file) for file in os.listdir(music_directory) if file.endswith(".mp3")]

current_track = 0
playing = False

def play_music():
    mixer.music.load(playlist[current_track])
    mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    mixer.music.pause()
                    playing = False
                else:
                    mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(playlist)
                play_music()
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(playlist)
                play_music()

    
    screen.blit(background, (0, 0))
    screen.blit(play_button if not playing else pause_button, (200, 250))
    screen.blit(next_button, (300, 250))
    screen.blit(prev_button, (380, 250))

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
