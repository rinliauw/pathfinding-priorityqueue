
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
from .hexpath import HexPath
from .priorityQueue import PriorityQueue

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

    main_board = Board();
    board_dict = {}

    print(data)
    
    # makes object (token) from json file
    for team, descriptions in data.items():
        if descriptions == []:
            continue
        for description in descriptions:
            new_token = Token((description[1],description[2]), description[0], team);
            if team == 'upper':
                main_board.add_token_upper(new_token)
            elif team == 'lower':
                main_board.add_token_lower(new_token)
            elif team == 'block':
                main_board.add_token_block(new_token)

            if team == 'block':
                board_dict[(description[1], description[2])] = team
            else:
                board_dict[(description[1], description[2])] = description[0]

    main_board.find_token_paths()