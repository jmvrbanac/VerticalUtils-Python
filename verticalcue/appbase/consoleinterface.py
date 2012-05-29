'''
Quick and dirty base for console-based python utility apps.
Created on May 28, 2012
@author: John Vrbanac

'''

import re

class ConsoleInterface(object):
    __registeredCommands = []
    
    def add_command(self, name, callback):
        cmd = Command()
        cmd.command = name
        cmd.callback = callback
        self.__registeredCommands.append(cmd)
    
    def activate(self):
        uInput = "unused"
        while(len(uInput) > 1):
            userCommand = Command()
            userCommand.parse_command(input("Command:"))
            
            found = False
            results = ""
            for cmd in self.__registeredCommands:
                if cmd.command == userCommand.command:
                    found = True
                    results = cmd.call()
                
            if found == False:
                print("Unknown command")
            elif results == "terminate":
                return
        pass
    
    def __close(self, args):
        return "terminate"
        
    
    def __init__(self):
        self.add_command("quit", self.__close)
        pass


class Command(object):
    command = ""
    arguments = []
    callback = None
    
    def parse_command(self, inputString):
        matches = re.findall("(\\b[\\w=]+\\b)", inputString)
        if matches:
            for index in range(len(matches)):
                if index == 0:
                    self.command = matches[index]
                else:
                    self.arguments.append(matches[index])
                    
    def call(self):
        return self.callback(self.arguments)
        
    