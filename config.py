#!/usr/bin/env python3

#
#
#   
#    __   __ __   ______  ______  __  __   ______   __           ______   __  __   ______   ______    
#   /\ \ / //\ \ /\  == \/\__  _\/\ \/\ \ /\  __ \ /\ \         /\  ___\ /\ \/\ \ /\  == \ /\  ___\   
#   \ \ \'/ \ \ \\ \  __<\/_/\ \/\ \ \_\ \\ \  __ \\ \ \____    \ \ \____\ \ \_\ \\ \  __< \ \  __\   
#    \ \__|  \ \_\\ \_\ \_\ \ \_\ \ \_____\\ \_\ \_\\ \_____\    \ \_____\\ \_____\\ \_____\\ \_____\ 
#     \/_/    \/_/ \/_/ /_/  \/_/  \/_____/ \/_/\/_/ \/_____/     \/_____/ \/_____/ \/_____/ \/_____/ 
#
#    config.py
#
#   Anish Gupta
#   July 2024
#   https://github.com/neur0n-7/VirtualCube
#
#




# CAMERA SETTINGS
CAMERA_X = 150
CAMERA_Y = 200
FOCAL_LENGTH = 500

# DISPLAY SETTINGS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 720
FPS = 60

# COLORS
COLORS  = {
	"white": (241,244,237),
	"yellow": (246,241,41),
	"red": (255,57,38),
	"green": (37,219,53),
	"blue": (12,82,241),
	"orange": (250,138,45),
	"background": (20, 20, 20),
	"button_bg": (230, 230, 230),
	"fps": (255, 255, 255),
	"time": (255, 255, 255),
	"button_fg": (20, 20, 20),
	"border": (0, 0, 0),
	"interior": (50, 50, 50),
	"scrambling": (100, 100, 100)
}


"""
Alternate theme:

COLORS = {
    "white": (255, 255, 255),
    "yellow": (255, 223, 51),
    "red": (255, 69, 58),
    "green": (34, 193, 34),
    "blue": (50, 130, 184),
    "orange": (255, 159, 28),
    "background": (30, 30, 30),
    "button_bg": (240, 240, 240),
    "fps": (255, 255, 255),
    "time": (255, 255, 255),
    "button_fg": (30, 30, 30),
    "border": (50, 50, 50),
    "interior": (140, 140, 140),
    "scrambling": (140, 140, 140)
}

Alternate theme #2:

"""

# CUBE SETTINGS
SPIN_FACTOR = 0.9 # Higher = faster and vice versa, between 0 and 1
NORMAL_CUBE_TURN_SPEED = 7.5 # Should be a divisor of 90 (or very close to it)
SCRAMBLE_CUBE_TURN_SPEED = 30 # Should be a divisor of 90 (or very close to it)
SCRAMBLE_RANGE = (20, 30) # Min and max number of times to scramble
DRAW_INTERIOR = True # Whether or not to draw the interior of the cube

# INSTRUCTIONS SETTINGS
INSTRUCTIONS_DELAY_SECS = 0.5 # How long to wait before showing instructions
INSTRUCTIONS_FADE_SECS = 1# How long to fade instructions in
FADE_OUT_SECS = 0.25 # How long to fade instructions out
INSTRUCTION_GAP_FRAMES = 100 # How many frames between each instruction

# RESET SETTINGS
RESET_TYPE = "FADE" # "GLIDE" or "FADE"

if RESET_TYPE == "FADE":
	RESET_FADE_SECONDS = 0.25 # How long to fade out
	RESET_FADE_FRAMES = int(RESET_FADE_SECONDS*FPS)
	RESET_PAUSE_SECONDS = 0.25 # How long to pause after fading out before fading in again

SHOW_FPS = True

AVERAGE_DIST_SORTING = False # If this is false, sorting will only take average Z position into account instead of X, Y, and Z

if __name__ == "__main__":
	print("To run Virtual Cube, run main.py instead of this file (config.py).")
