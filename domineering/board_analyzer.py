def count_safe_moves_horizontal(board, skip_ahead=True):
    return __count_moves_with_property_horizontal(board, lambda x: is_safe_move(board, x, False), skip_ahead)


def count_safe_moves_vertical(board, skip_ahead=True):
    return __count_moves_with_property_vertical(board, lambda x: is_safe_move(board, x, True), skip_ahead)


def is_safe_move(board, move, vertical):
    if not can_make_move(board, move, vertical):
        return False
    if vertical:
        on_left_border = __is_vertical_move_on_left_border(board, move)
        on_right_border = __is_vertical_move_on_right_border(board, move)
        return on_left_border and on_right_border
    else:
        on_upper_border = __is_horizontal_move_on_upper_border(board, move)
        on_lower_border = __is_horizontal_move_on_lower_border(board, move)
        return on_upper_border and on_lower_border


def is_border_move(board, move, vertical):
    if vertical:
        return __is_vertical_border_move(board, move)
    else:
        return __is_horizontal_border_move(board, move)


def __is_vertical_border_move(board, move):
    on_left_border = __is_vertical_move_on_left_border(board, move)
    on_right_border = __is_vertical_move_on_right_border(board, move)
    return on_left_border or on_right_border


def __is_vertical_move_on_left_border(board, move):
    row, col = move
    left_upper = row, col - 1
    left_lower = row + 1, col - 1
    left = [left_upper, left_lower]
    return board.positions_are_occupied(left)


def __is_vertical_move_on_right_border(board, move):
    row, col = move
    right_upper = row, col + 1
    right_lower = row + 1, col + 1
    right = [right_upper, right_lower]
    return board.positions_are_occupied(right)


def __is_horizontal_border_move(board, move):
    on_upper_border = __is_horizontal_move_on_upper_border(board, move)
    on_lower_border = __is_horizontal_move_on_lower_border(board, move)
    return on_upper_border or on_lower_border


def __is_horizontal_move_on_upper_border(board, move):
    row, col = move
    upper_left = row - 1, col
    upper_right = row - 1, col + 1
    upper = [upper_left, upper_right]
    return board.positions_are_occupied(upper)


def __is_horizontal_move_on_lower_border(board, move):
    row, col = move
    lower_left = row + 1, col
    lower_right = row + 1, col + 1
    lower = [lower_left, lower_right]
    return board.positions_are_occupied(lower)


def count_moves_horizontal(board, skip_ahead=True):
    return __count_moves_with_property_horizontal(board, lambda x: can_make_move(board, x, False), skip_ahead)


def count_moves_vertical(board, skip_ahead=True):
    return __count_moves_with_property_vertical(board, lambda x: can_make_move(board, x, True), skip_ahead)


def __count_moves_with_property_vertical(board, prop, skip_ahead=True):
    count = 0
    col = 0
    while col < board.get_width():
        row = 0
        while row < board.get_height():
            if prop((row, col)):
                count += 1
                if skip_ahead:
                    row += 2
                    continue
            row += 1
        col += 1
    return count


def __count_moves_with_property_horizontal(board, prop, skip_ahead=True):
    count = 0
    row = 0
    while row < board.get_height():
        col = 0
        while col < board.get_width():
            if prop((row, col)):
                count += 1
                if skip_ahead:
                    col += 2
                    continue
            col += 1
        row += 1
    return count


def can_make_move(board, move, vertical):
    row, col = move
    if vertical:
        return board.positions_are_empty([(row, col), (row+1, col)])
    else:
        return board.positions_are_empty([(row, col), (row, col+1)])
