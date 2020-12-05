from pynput import keyboard
from V7xStyle import Animation
An = Animation
def get_key_name(Key):
    if isinstance(Key,keyboard.KeyCode):
        return Key.char
    else:
        return str(Key)

def on_press(Key):
    key_name = get_key_name(Key)
    print("Key {} pressed".format(key_name))

def on_released(Key):
    key_name = get_key_name(Key)
    print("The Key {} Released".format(Key))
    if str(Key) == 'Key.esc':
        print("Loading Exiting  ==>>")
        An.Loading()
        return False



with keyboard.Listener(
    on_press = on_press,
    on_released = on_released)as listenter:
        listenter.join()