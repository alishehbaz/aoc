# Ref: https://adventofcode.com/2022/day/2

def p2():
    
    with open('input.txt') as f:
        strategies = [line.strip() for line in f]

    # A Y => 4
    # B X => 1
    # C Z => 7
    
    roundsScore = 0
    
    WIN = 6
    DRAW = 3
    LOSS = 0

    scores = {
        'A': 1, 'B': 2, 'C':3,
        'X': 1, 'Y': 2, 'Z':3
    }


    for strategy in strategies:
        opponent, you = strategy.split(' ')
        # Loss
        if you  == 'X': 
            movePoints = (scores[opponent]-1) % 3 
            if movePoints == 0:
                movePoints = 3
            roundsScore += LOSS + movePoints

        # Draw 
        if you == 'Y':
            roundsScore += DRAW + scores[opponent]

        # Win
        if you == 'Z':
            movePoints = (scores[opponent]+1)
            if opponent == 'C':
                movePoints = movePoints % 3
            roundsScore += WIN + movePoints

    return roundsScore

ans = p2()
print(f'total score based on strategy guide = {ans}')
