from pynput.keyboard import Key, Listener

class keyboardLogger():

    def on_press(self, key):
        print('{0} pressed'.format(key))
    
    def createKeyboardListener(self):
        with Listener(on_press=keyboardLogger().on_press) as listener:
            listener.join()
        
        