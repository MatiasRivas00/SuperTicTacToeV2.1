import CheckWin
import math
max_depth = 0


def best_move(board):
    BoardMatrix = board
    bestScore = -math.inf
    move = (0, 0)
    for i in range(8):
        for j in range(4):
            if BoardMatrix[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False, max_depth, -math.inf, math.inf)
                board[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    move = (i, j)
    return move


def minimax(board, depth, maximizing, md, alpha, beta):
    scores = {"X": -10, "O": 10, "tie": 0}
    result, pl = CheckWin.check_win(board)
    if depth >= md:
        return 0

    elif result:
        return scores[pl]

    elif is_full(board):
        return 0

    elif maximizing:
        bestScore = -math.inf
        for i in range(8):
            for j in range(4):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True, md, alpha, beta)
                    board[i][j] = " "
                    bestScore = max(score, bestScore)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return bestScore

    else:
        bestScore = math.inf
        for i in range(8):
            for j in range(4):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True, md, alpha, beta)
                    board[i][j] = " "
                    bestScore = min(bestScore, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return bestScore


def is_full(board):
    for i in range(8):
        for j in range(4):
            if board[i][j] == " ":
                return False
    return True
