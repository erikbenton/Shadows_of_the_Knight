import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if bomb_dir == "U":
    elif bomb_dir == "UR":
    elif bomb_dir == "R":
    elif bomb_dir == "DR":
    elif bomb_dir == "D":
    elif bomb_dir == "DL":
    elif bomb_dir == "L":
    elif bomb_dir == "UL":

    # the location of the next window Batman should jump to.
    print("0 0")