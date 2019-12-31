"""
This is a project suggested by Al Sweigart in his fun and instructive book "Automate the Boring Stuff".
From Chapter 11 on web scraping:  "Write a program that will open the game at https://gabrielecirulli.github.io/2048/
and keep sending up, right, down, and left keystrokes to automatically play the game."

Note program requires two installations:
(1) The Selenium module. I installed it using pip: https://pypi.org/
(2) WebDriver for Chrome that can be found here: https://chromedriver.chromium.org/home
I am curious if will run as is with a driver for another browser.

Here as some interesting ideas for extending this program:

(1)  Play until no further moves are possible.   Checking for game over after each move.
(2)  Retrieve final score date.
(3)  Play multiple games in succession.
(4)  My daughter claims that you can score higher by eliminating one of the movements.   For example never
cursor dowm.   Use the program to generate data to check this claim.
(5)  Incorporate some strategy into the cursor movement choices.   One possibility is to check for matching
tiles in rows or columns and move these tiles together.
(6)  Incorporate machine learning to design movement strategies.

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time, random

DELAY = 0.20 # Time delay in seconds used to for the wait() function.
PLAYS = 50 # Number of times program will click on the arrow keys.
SCROLL_TO = 270 # Number of pixels to scroll down the page in order to center it.

key_list = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT] # List of key attributes used by the Selenium module.
pressed_key = None # Keeps track of key that is pressed after each move.   Initialized as None for the initial board.

# A function that waits for the time given by the DELAY constant.   The function is used to give
# the game web page time to complete actions.
def wait():
    time.sleep(DELAY)

# Opens the Chrome browser
driver = webdriver.Chrome()
driver.maximize_window() # Maximizes the size of the browser window

# Opens the link for the 2048 game in the Chrome browser
driver.get('https://gabrielecirulli.github.io/2048/')
wait() # Give the page some time to load.

# Finds the HTML page element.   This element receives the cursor movement commands.
pageElem = driver.find_element_by_tag_name('html')

# Runs a short script to scroll down the page so that it is centered.
driver.execute_script("window.scrollTo(0, {});".format(SCROLL_TO))
wait() # Give the page time to scroll.

tile_pos_list = []

for i in range(PLAYS + 1):
    # Prints a heading for the state of the board after each move.
    print('\n')
    print('*' * 20)
    print('board number = {}'.format(i))
    print('pressed key = {}'.format(pressed_key))
    print('*' * 20)

    # Retrieve the tile position and tile values at the beginning of the game and after each move.
    elem1 = driver.find_element_by_class_name('tile-container').get_attribute('innerHTML')
    elem2 = driver.find_elements_by_class_name('tile-inner')

    pos_list = []
    junk_list = []

    for junk in elem2:
        junk_list.append(int(junk.text))
    for n in range(len(elem1)):
        if elem1[n:n + 13] == 'tile-position':
            pos_list.append((int(elem1[n + 16]), int(elem1[n + 14])))
    # Creates a dictionary for each board with the position as the key and the tile value as the value.
    tile_pos = dict(zip(pos_list, junk_list))
    tile_pos_list.append(tile_pos)


    print('board dictionary = ', tile_pos)
    print('*' * 16*len(tile_pos))

    # Randomly selects a cursor button and presses it
    pressed_key = key_list[random.randrange(4)]
    pageElem.send_keys(pressed_key)
    wait()  # Allow some time for key strokes.


"""
Can use this code to start a new game.
elem = driver.find_element_by_link_text('New Game')
elem.click()
"""
