# Ref: https://adventofcode.com/2022/day/2

def p1():
    with open('input.txt') as f:
        strategies = [line.strip() for line in f]

    roundsScore = 0

    WIN = 6
    DRAW = 3
    LOSS = 0

    scores = {
        'A': 1, 'B': 2, 'C': 3,
        'X': 1, 'Y': 2, 'Z': 3
    }

    equivalncies = {
        'A': 'X', 'B': 'Y', 'C': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C'
    }

    results = {
        # rock beats scissors
        'A': 'C', 'X': 'Z',
        # paper beats rock
        'B': 'A', 'Y': 'X',
        # scissor beats paper
        'C': 'B', 'Z': 'Y',
    }

    for strategy in strategies:
        opponent, you = strategy.split(' ')
        # Loss
        if equivalncies[results[opponent]] == you:
            roundsScore += LOSS + scores[you]

        # Draw
        elif scores[opponent] == scores[you]:
            roundsScore += DRAW + scores[you]

        # Win
        else:
            roundsScore += WIN + scores[you]

    return roundsScore


ans = p1()
print(f'total score based on strategy guide = {ans}')
