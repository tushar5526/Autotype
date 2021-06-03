from pynput.keyboard import Key, Controller
from time import sleep
from argparse import ArgumentParser
import os, sys

def type(path=None, delay=None):
    if not delay:
        delay = 3
    
    # wait for few seconds before typing
    sleep(delay)
    
    # manually enter your code here or provide a path
    code = """
class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    """
    if path:
        with open(path, 'r') as file:
            code = file.read()
        
    keyboard = Controller()
    for line in code.split('\n'):
        keyboard.type(line)
        keyboard.tap(Key.enter)
        keyboard.tap(Key.home)
    
if __name__ == '__main__':
    parser = ArgumentParser(description='Autotype the specified file')
    parser.add_argument('-p', '--path',
                        metavar='path',
                        type=str,
                        help='the path to the file')
    parser.add_argument('-t', '--time',
                        metavar='time',
                        type=int,
                        help='time delay before typing')
    
    args = parser.parse_args()
    path = args.path
    delay = args.time
    if path and not os.path.isfile(path):
        print('No such file exists. Input the correct path!')
        sys.exit(0)
    type(path, delay)
