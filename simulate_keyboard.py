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
            Enter the code to be autotyped 
            here or provide a path to the file 
    """
    if path:
        with open(path, 'r') as file:
            code = file.read()
            print(code)
        
    keyboard = Controller()
    keyboard.type(code)
    
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
