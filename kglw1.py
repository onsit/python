import pygame
import cv2
import numpy as np
from PIL import Image
import os

print("Current working directory:", os.getcwd())

# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("King Gizzard VHS Bootleg Display")
clock = pygame.time.Clock()

# Load assets (ensure these files exist in the correct paths)
audio_files = ["C:/Users/Reid/python/KGLW/gila.wav"]
video_files = ["C:/Users/Reid/python/KGLW/footy.mp4"]
album_art = ["C:/Users/Reid/python/KGLW/gizart.png"]

# Check if files exist
for file_list in [audio_files, video_files, album_art]:
    for file in file_list:
        if not os.path.exists(file):
            print(f"Error: File not found - {file}")
            print("Make sure the file exists in the correct directory.")
            exit()

current_track = 0

# Load initial audio
try:
    pygame.mixer.music.load(audio_files[current_track])
    pygame.mixer.music.play()
except pygame.error as e:
    print(f"Error loading audio: {e}")
    exit()

# VHS effect function
def apply_vhs_effect(frame):
    """Apply a VHS-like effect to the video frame."""
    # Add noise
    noise = np.random.normal(0, 25, frame.shape).astype(np.uint8)
    frame = cv2.add(frame, noise)
    # Add scanlines
    for i in range(0, frame.shape[0], 4):
        frame[i:i+2, :] = frame[i:i+2, :] * 0.9
    # Slight color distortion
    frame[:, :, 2] = cv2.add(frame[:, :, 2], 10)  # Boost red channel
    return frame

# Load video capture
cap = cv2.VideoCapture(video_files[current_track])
if not cap.isOpened():
    print(f"Error: Unable to open video file - {video_files[current_track]}")
    exit()

# Load album art
try:
    art_image = pygame.image.load(album_art[current_track])
    art_image = pygame.transform.scale(art_image, (screen_width, screen_height))
except pygame.error as e:
    print(f"Error loading album art: {e}")
    exit()

# Main loop
running = True
show_art = False
art_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Switch between video and art every 10 seconds
    art_timer += 1
    if art_timer > 600:  # ~10 seconds at 60 FPS
        show_art = not show_art
        art_timer = 0

    if show_art:
        screen.blit(art_image, (0, 0))
    else:
        ret, frame = cap.read()
        if not ret:  # Restart video if it ends
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = cap.read()

        if ret:
            # Apply VHS effect
            frame = apply_vhs_effect(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)  # Rotate for Pygame
            frame_surface = pygame.surfarray.make_surface(frame)
            frame_surface = pygame.transform.scale(frame_surface, (screen_width, screen_height))
            screen.blit(frame_surface, (0, 0))

    # Check if audio ended, switch to next track
    if not pygame.mixer.music.get_busy():
        current_track = (current_track + 1) % len(audio_files)
        try:
            pygame.mixer.music.load(audio_files[current_track])
            pygame.mixer.music.play()
        except pygame.error as e:
            print(f"Error loading audio: {e}")
            running = False

        cap = cv2.VideoCapture(video_files[current_track])
        if not cap.isOpened():
            print(f"Error: Unable to open video file - {video_files[current_track]}")
            running = False

        try:
            art_image = pygame.image.load(album_art[current_track])
            art_image = pygame.transform.scale(art_image, (screen_width, screen_height))
        except pygame.error as e:
            print(f"Error loading album art: {e}")
            running = False

    # Simulate CRT bezel
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, screen_width, screen_height), 20, border_radius=20)

    pygame.display.flip()
    clock.tick(60)

# Cleanup
cap.release()
pygame.quit()