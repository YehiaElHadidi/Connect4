from board import COMPUTER_PIECE, PLAYER_PIECE, COLUMN_COUNT, ROW_COUNT, WINDOW_LENGTH


def is_terminal(board, valid_locations):
    return wining_move(board, COMPUTER_PIECE) or wining_move(board, PLAYER_PIECE) or len(valid_locations) == 0


def wining_move(board, piece):

    # Check horizontal locations to win
    for c in range(COLUMN_COUNT - 3):  # No need to check last 3 columns
        for r in range(ROW_COUNT):
            # Check if there are 4 consecutive pieces in any row
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # check vertical locations to win
    for r in range(ROW_COUNT-3):  # no need to check last 3 rows
        for c in range(COLUMN_COUNT):
            # check if thier is 4 consecutive piece in any coloumn
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # check diagonal locations to win (from buttom to top)
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # check diagonal locations to win (from top to down)
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False


def score_position(brd, piece):
    # Score Horizontal
    score = 0
    for r in range(ROW_COUNT):
        row_array = brd.board[r]
        for c in range(COLUMN_COUNT-3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [row[c] for row in brd.board]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Score positive sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [brd.board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    # Score negative sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [brd.board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score


def evaluate_window(window, piece):
    score = 0

    opp_piece = COMPUTER_PIECE
    if piece == COMPUTER_PIECE:
        opp_piece = PLAYER_PIECE

    piece_count = window.count(piece)  # count occurence
    empty_count = window.count(0)

    if (piece_count == 4):
        score += 1000  # highest score we can get
    elif (piece_count == 3) and empty_count == 1:
        score += 10
    elif (piece_count == 2) and empty_count == 2:
        score += 5

    opp_count = window.count(opp_piece)
    if opp_count == 3 and empty_count == 1:
        score -= 900

    return score
