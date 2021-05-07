#this python file is for utility function

def distance(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    z1 = - x1 - y1
    x2 = point2[0]
    y2 = point2[1]
    z2 = - x2 - y2
    return (abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)) / 2

def calc_h_cost(current, end):
    return distance(current, end)

def calc_f_cost(current, end, g_cost):
    return calc_h_cost(current, end) + g_cost

#check if the position is inside the board range
def inside_board(position):
    #convert to cube coordinate for easier calculation
    x = position[0]
    y = position[1]
    z = - x - y
    if (abs(x) <= 4) & (abs(y) <= 4) & (abs(z) <= 4) & ((x + y + z) == 0):
        return True
    else:
        return False

#a function that return all the neighbours of a position
def get_neighbours(position):
    axial_movement = [(1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)]

    neighbours_list = []
    r = position[0]
    q = position[1]

    for dr, dq in axial_movement:
        new_r = r + dr
        new_q = q + dq
        if inside_board((new_r, new_q)):
            neighbours_list.append((r + dr, q+ dq))
    return neighbours_list

#this funtion will return a tupple of 2 index which has the same data
def find_duplicate(target_list):
    for i in range(len(target_list)):
        for j in range(1, len(target_list)):
            if (target_list[i] == target_list[j]):
                return (i, j)
    return None

#this function will rturn a list of possible swing positions
def get_swing_position(current_position, swing_position):
    axial_movement = [(1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)]
    swing_movement = []
    swing_diff = [-1, 0, 1]
    position_result = []

    # finds difference between current and ally
    (dx, dy) = (swing_position[0] - current_position[0], swing_position[1] - current_position[1])
    for i in range(len(axial_movement)):
        if (dx, dy) == axial_movement[i]:
            break

    # if the difference is in index 0
    if i == 0:
        swing_movement.append(axial_movement[0])
        swing_movement.append(axial_movement[-1])
        swing_movement.append(axial_movement[1])
    # if it is everywhere else
    else:
        for diff in swing_diff:
            swing_movement.append(axial_movement[i + diff - len(axial_movement)])

    for dr, dq in swing_movement:
        position_result.append((swing_position[0] + dr, swing_position[1] + dq))

    for pos in position_result:
        if not inside_board(pos):
            del pos

    if position_result == []:
        return None
    return position_result

def get_board_value(board){
    
}