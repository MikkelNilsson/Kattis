s = int(input())

# Calculate positions
def position_calculation(s):
    return s + int(s/13) + 15

def get_tuple_coord(val):
    y = val % 10
    x = int((val - y) / 10)
    return (x, y)

positions = set()
while(len(positions) < 4):
    s = position_calculation(s)
    positions.add(get_tuple_coord(s % 100))


# Measure distances
def measure_distance(pos):
    min_dist = 10**6
    for (x,y) in positions:
        dist = abs(pos[0] - x) + abs(pos[1] - y)
        if dist < min_dist:
            min_dist = dist

    return min_dist


# the GAME
moves = 0
while (len(positions) > 0):
    moves += 1
    pos = get_tuple_coord(int(input()))

    if pos in positions:
        positions.remove(pos)
        print("You hit a wumpus!")
    
    if len(positions) > 0:
        print(measure_distance(pos))

    else:
        print(f"Your score is {moves} moves.")
