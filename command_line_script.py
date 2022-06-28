from argparse import ArgumentParser
import os, sys
from Simulator.simulate_keyboard import Type
    
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
    Type(path, delay)
