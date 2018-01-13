"""
 Sample code for SI 507 Waiver Assignment
 University of Michigan School of Information
 Based on "Pygame base template for opening a window" 
     Sample Python/Pygame Programs
     Simpson College Computer Science
     http://programarcadegames.com/
     http://simpson.edu/computer-science/
 
See README for the assignment for instructions to complete and submit this.
"""
 
import pygame
import random
import test
import wikipedia
import nltk
from nltk.probability import FreqDist

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

input_text = input ("input a string: ")
print("Game loading...Please wait!")
test_list = []
wiki_search = wikipedia.search(input_text,results=5)

for result1 in wiki_search:
    long_paragraph = wikipedia.summary(result1)
    seperated_text = nltk.word_tokenize(long_paragraph)
    speech_tag = nltk.pos_tag(seperated_text)
    for ele in speech_tag:
        if ele[1] == 'JJ':
            test_list.append(ele[0])
    f_list = FreqDist(test_list)
    f_count = FreqDist(test_list).items()
    f_word = f_list.keys()
    sorted_words = sorted(f_count, key = lambda f_word:f_word[1], reverse = True)
    big_word_list = [x[0] for x in sorted_words]
    sample_pos_dict = {"JJ" : sorted_words}

# You must construct a dictionary of this form from your wikipedia search
# See test.py for more details on the format requirements for the dictionary

# You must leave this line in your submission, and you must pass the test!
if test.test(sample_pos_dict):
    print ("You passed this sample_pos_diction part of the test!")
else:
    print ("You didn't pass. Please try again")

# This is the temp word list for testing.
# You will need to **replace this** with words extracted from your wikipedia search.
# See README for more details.
word_list = big_word_list[:6]
first_word = [y[0] for y in word_list]

# The class that manages the balls shown on the screen in the game.
class BallManager:

    INIT_SPEED = 1
    current_index = 0

    def __init__(self):
        self.max_balls = 3
        self.active_balls = []
        for w in word_list: 
            self.active_balls.append(WordBall(w, self.INIT_SPEED))

    def create_ball(self, word):
        self.active_balls.append(WordBall(word, self.INIT_SPEED))
    
    def num_balls(self):
        return len(self.active_balls)

    def remove_balls(self, index):
        self.active_balls.pop(index)

    def __str__(self):
        s = ''
        for b in self.active_balls:
            s += b.word + ", "
        return s

# The class for each ball showing on the screen.
# You can play around with size, color, font, etc. 
class WordBall:

    def __init__(self, word, speed):
        self.word = word
        self.x_pos = random.randint(0, pygame.display.Info().current_w)
        self.y_pos = 0
        self.height = 100
        self.width = 100
        self.speed = speed

    def move_ball(self):
        self.y_pos += self.speed
        if (self.y_pos > pygame.display.Info().current_h - self.height):
            self.y_pos = 0

# Initialize game
pygame.init()

size = (1000, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Type to Win")
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button...

ball_manager = BallManager()
ball_font = pygame.font.Font(None, 36)
keys_font = pygame.font.Font(None, 60)
gameover_font = pygame.font.Font(None, 80)
done = False
game_over = False
keys_typed = ''

def show_game_over_screen():
    screen.fill(BLACK)
    gameSurf = gameover_font.render('Game Over!',1, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.centerx = pygame.display.Info().current_w / 2
    gameRect.centery = pygame.display.Info().current_h / 2
    screen.blit(gameSurf, gameRect)
    pygame.display.flip()
    waiting = True
    while waiting: 
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

# Main display loop
while not done:
    
    if game_over:
        show_game_over_screen()

    # Handle input events.
    key = ''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            key = event.unicode
            keys_typed += key
            for ball in ball_manager.active_balls:
                if ball.word[0] == key:
                    index = ball_manager.active_balls.index(ball)
                    ball_manager.remove_balls(index)

    #print(type(ball_manager.active_balls)) active balls is a list with 5 balls

    for b in ball_manager.active_balls:
        b.move_ball()

    # Blank the screen
    screen.fill(WHITE)

    # Render game objects
    for ball in ball_manager.active_balls:
        pygame.draw.ellipse(screen, RED, [ball.x_pos, ball.y_pos, ball.width, ball.height]) 
        text = ball_font.render(ball.word, 1, BLACK)
        textpos = text.get_rect()
        textpos.centerx = ball.x_pos + ball.width / 2
        textpos.centery = ball.y_pos + ball.height / 2
        screen.blit(text, textpos)

 
    text = keys_font.render('keys typed: ' + keys_typed, 1, GREEN)
    textpos = text.get_rect()
    textpos.centerx = pygame.display.Info().current_w / 2
    textpos.centery = pygame.display.Info().current_h - 30
    screen.blit(text, textpos)


    # Update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

    if ball_manager.active_balls == []:
        game_over = True
# Close the window and quit.
pygame.quit()
