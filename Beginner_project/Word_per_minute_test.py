import curses
from curses import color_pair, wrapper
import time
import random

#step 2 create a screen start function.

def screen_start(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to typing speed test game !", curses.color_pair(1))
    stdscr.addstr(2,1,"Press any key to continue : ", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()

#step 4 overlaying text
def display_text(stdscr , target , current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM : {wpm}") #to concat two strings

    for i,char in enumerate(current):  #we loop through every char in current text
        current_char = target[i]
        color = curses.color_pair(1)
        if char != current_char:
            color = curses.color_pair(2)

        stdscr.addstr(0,i,char , color)  
#step 6 - load sentences from text file.
def load_text():
    with open("Test_text.txt","r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

#step 3 - word per min fucntion
def wpm_test(stdscr):
    # target_text = "Hello this is the test text which you need to see and type in minimum time !"
    # Or 
    # load text from file
    target_text = load_text()
    current_text = []
    #step 5 wpm time calculations
    wpm = 0
    start_time = time.time()  #keeping track of start time of words
    stdscr.nodelay(True)
    
    while True:
        time_elapsed = max(time.time() - start_time, 1) 
        wpm = round((len(current_text) / (time_elapsed/60))/5)
        #time.time() gives current time. so to get time lapsed between current time and start_time we used time_elapsed
            
        stdscr.clear()
        #the below login is now added in step 4
        # stdscr.addstr(target_text)

        # for char in current_text:  #we loop through every char in current text
        #     stdscr.addstr(char , curses.color_pair(1))  #we display char from current text
        display_text(stdscr,target_text,current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:  #it will join list and string
            stdscr.nodelay(False)  # we need to get rid of this nodelay if user is pressing the key
            break

        try:
            key = stdscr.getkey()  #we asking user to type something so as soon as they type something it is stored in current_text
        except:
            continue   #brings back to while loop if user doesnt enter any key

        if ord(key) == 27:  #esc key on keyboard is represented by ordinal value of 27. each key on keyb has unique ord value
            break   #to find way out of loop , if user typw esc loop will break

        if key in ("KEY_BACKSPACE","\b", "\x7f"): #if the user press backspace he/she should delete the character
            if len(current_text) > 0:
                current_text.pop()   #delete last letter from current text list
        elif len(current_text) < len(target_text):#if the user is typing the char more then target text he will get an exception,
            current_text.append(key)                                 #then he should not type more then target text
             


# step 1 : we created the main function which has  colors with the help of curses module
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN , curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED , curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE , curses.COLOR_BLACK)

    screen_start(stdscr)#calling sreen function
    while True:  # just the user can play again the game. if user press esc then game over
        wpm_test(stdscr)

        stdscr.addstr(2,0,"you completed the test, please press any key to continue...")
        key = stdscr.getkey()
        if ord(key) == 27:
          break
            

wrapper(main)