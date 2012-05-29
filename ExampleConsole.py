'''
Created on May 28, 2012
@author: John Vrbanac
'''
from verticalcue.appbase.consoleinterface import ConsoleInterface

def sample_command(args):
    print("This is a sample command")

if __name__ == '__main__':
    console = ConsoleInterface()
    console.add_command("sample", sample_command)
    console.activate()