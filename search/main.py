
"""
COMP30024 Artificial Intelligence, Semester 1, 2021
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json
from .token import Token
from .board import Board

# from .board import Board

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from search.util import print_board, print_slide, print_swing

def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)

    # board = Board(4);

    # bikin tokennya
    # mskin ke board

    dict = {}
    count = 1

    tokens_list = []
    # makes object (token) from json file
    for i in data.keys():
        #print(data[i]);
        for j in data[i]:
            #print(j);
            token = Token((j[1],j[2]), j[0], i);
            tokens_list.append(token)
            #how to make multiple tokens?
            print(count, token.category, token.team, token.position)
            count += 1
    print(tokens_list)

    # adds tokens to board
    board_state = Board(tokens_list)
    print(board_state)

    #token1 = Token((1, 1), 's', 'upper')
    #print(token1.category)
    #print(token1.team)

    # TODO:
    # Find and print a solution to the board configuration described
    # by `data`.
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).
