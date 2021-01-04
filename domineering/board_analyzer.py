def count_safe_moves_horizontal(board, skip_ahead=True):
    return __count_moves_with_property_horizontal(board, lambda x: is_safe_move(board, x, False), skip_ahead)


def count_safe_moves_vertical(board, skip_ahead=True):
    return __count_moves_with_property_vertical(board, lambda x: is_safe_move(board, x, True), skip_ahead)


def is_safe_move(board, move, vertical):
    if not can_make_move(board, move, vertical):
        return False
    row, col = move
    if vertical:
        left_upper = row, col - 1
        left_lower = row + 1, col - 1
        right_upper = row, col + 1
        right_lower = row + 1, col + 1
        return board.positions_are_occupied([left_upper, left_lower, right_upper, right_lower])
    else:
        upper_left = row - 1, col
        upper_right = row - 1, col + 1
        lower_left = row + 1, col
        lower_right = row + 1, col + 1
        return board.positions_are_occupied([upper_left, upper_right, lower_left, lower_right])


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
