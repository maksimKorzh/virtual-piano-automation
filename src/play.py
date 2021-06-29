########################################
#
# Python script to automatically play
#    music sheets on Virtual Piano
#    (https://virtualpiano.net/)
#
#                by
#
#         Code Monkey King
#
########################################

# packages
import pyautogui as pg
import time

# wait until user navigates to "https://virtualpiano.net/"
print('Please navigate to "https://virtualpiano.net/"')
print('Make sure that piano has loaded and you have')
print('your browser window with virtual piano in focus!')
print('Music would startplaying in 5 sec...')
time.sleep(5)

# =====================================
# Preferred delays for different pieces
# =====================================
#
# Interstellar Main Theme:          0.1
# Yiruma - River flows in you:     0.03
# Amélie Valse                      0.1
# Comptine d'un autre été (Amélie) 0.08

# delay between notes (change tempo)
delay = 0.03

# open music sheet
with open('sheet.txt') as f:
    # init notes
    notes = f.read()
    
    # init index
    index = 0
    
    # loop over notes
    while index in range(len(notes)):
        if notes[index].isalpha() or notes[index].isdigit():
            # mimic piano key press
            pg.press(notes[index])
            
            # print pressed key
            print("pressed key:", notes[index])
        
        else:
            # handle long notes
            if notes[index] == '|': time.sleep(delay * 8)
            
            # handle chords
            if notes[index] == '[':
                # define chord list
                chord = []
                
                # parse chord
                while notes[index] != ']':
                    # append note to chord
                    if notes[index].isalpha() or notes[index].isdigit():
                        # append note to chord
                        chord.append(notes[index])
                    
                    # go to next note within a chord
                    index += 1
                
                # mimic piaono chord play
                exec('pg.hotkey(' + str(chord)[1: -1] + ')')
                
                # print pressed keys
                print("pressed keys:", chord)

        # default pause between notes
        time.sleep(delay)
            
        # skip to the next note
        index += 1        

print('Thanks for listening!')




