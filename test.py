import pygame
import time

# Initialize the pygame mixer
pygame.mixer.init()

# Create a pygame Sound object by loading an MP3 file
pygame.mixer.music.load("assets/loops/808-bass-boom-hard-trap-loop-8-11510.mp3")

# Play the MP3 file
pygame.mixer.music.play()

# Wait for the audio to finish playing (optional)
while pygame.mixer.music.get_busy():
    time.sleep(1)
