class Pattern:
    def __init__(self, pattern, row_nr, col_nr, vertical):
        self.pattern = pattern
        self.row_nr = row_nr
        self.col_nr = col_nr
        self.vertical = vertical


class PatternSearch:
    def count_occurrences_of_pattern(self, board, pattern, skip_ahead=False, restrictions=None):
        if pattern.vertical:
            return self.__count_occurrences_of_vert_pattern(board, pattern, skip_ahead, restrictions=restrictions)
        else:
            return self.__count_occurrences_of_hor_pattern(board, pattern, skip_ahead, restrictions=restrictions)

    def __count_occurrences_of_vert_pattern(self, board, pattern, skip_ahead=False, restrictions=None):
        count = 0
        pattern_row_nr = pattern.row_nr
        pattern_col_nr = pattern.col_nr
        col_start, col_end = self.__determine_col_restrictions(
            restrictions, board, pattern_col_nr)
        row_start, row_end = self.__determine_row_restrictions(
            restrictions, board, pattern_row_nr)
        for col_index in range(col_start, col_end):
            row_index = row_start
            while row_start <= row_index < row_end:
                if self.__pattern_starts_at(board, row_index, col_index, pattern):
                    count += 1
                    if skip_ahead:
                        row_index += pattern_row_nr
                        continue
                row_index += 1
        return count

    def __count_occurrences_of_hor_pattern(self, board, pattern, skip_ahead=False, restrictions=None):
        count = 0
        pattern_row_nr = pattern.row_nr
        pattern_col_nr = pattern.col_nr
        col_start, col_end = self.__determine_col_restrictions(
            restrictions, board, pattern_col_nr)
        row_start, row_end = self.__determine_row_restrictions(
            restrictions, board, pattern_row_nr)
        for row_index in range(row_start, row_end):
            col_index = col_start
            while col_start <= col_index < col_end:
                if self.__pattern_starts_at(board, row_index, col_index, pattern):
                    count += 1
                    if skip_ahead:
                        col_index += pattern_col_nr
                        continue
                col_index += 1
        return count

    def __determine_col_restrictions(self, restrictions, board, pattern_col_nr):
        if restrictions and 'col' in restrictions:
            start_restriction, end_restriction = restrictions['col']
            return max(start_restriction, 0), min(len(board[0])-pattern_col_nr+1, end_restriction)
        return 0, len(board[0])-pattern_col_nr+1

    def __determine_row_restrictions(self, restrictions, board, pattern_row_nr):
        if restrictions and 'row' in restrictions:
            start_restriction, end_restriction = restrictions['row']
            return max(start_restriction, 0), min(len(board)-pattern_row_nr+1, end_restriction)
        return 0, len(board)-pattern_row_nr+1

    def __pattern_starts_at(self, board, row_index, col_index, pattern):
        pattern_row_nr = pattern.col_nr
        row_patterns = pattern.pattern
        for pattern_row_ind, pattern_row in enumerate(row_patterns):
            line_section = board[row_index +
                                 pattern_row_ind][col_index:col_index + pattern_row_nr]
            if not all([line_section[pos] in pattern_row[pos] for pos in pattern_row]):
                return False
        return True
