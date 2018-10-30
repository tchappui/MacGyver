#! /usr/bin/env python3
# coding: utf-8

# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------

import os
import pygame
from pygame.locals import *

import readJSON

# ----------------------------------------------------------------
#                      VARIABLE INITIALIZATION
# ----------------------------------------------------------------

conf = None
keep_playing = True
player_choice = None
quit_game = False

# ----------------------------------------------------------------
#                      CORE OF THE GAME
# ----------------------------------------------------------------

#Initialization of pygame
pygame.init()

#Center the window of the game at the center of the computer screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

conf = readJSON.jsonToDictionary()

while quit_game == False:
    #display title screen

    #Depending on the choice in the title screen, display the right thing
    pass