def isValidMove(movement):
    isValid = False
    validMove = ['E', 'W', 'R', 'X']

    if len(movement) <= 4:
        for move in movement:
            if move in validMove:
                isValid = True
                validMove.remove(move)
            else:
                isValid = False
                break

    return isValid