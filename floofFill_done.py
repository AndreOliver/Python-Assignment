"""
Andre Oliver
Assignment 3
Programming Languages
----------------------------------
Python Assignment
Complete the implementation below of the flood fill algorithm.

All your code should go into the floodFill function.
You will know your solution is correct when the program
prints out a success message to the screen.

"""

import sys

textmap = """
....................
.......XXXXXXXXXX...
.......X........X...
.......X........X...
..XXXXXX........X...
..X.............X...
..X.............X...
..X........XXXXXX...
..X........X........
..XXXX..XXXX........
.....XXXX...........
....................
....................
"""

lines = textmap.strip().split('\n')
assert ['bad width' for x in lines if len(x) != len(lines[0])] == [], "WORLD string needs to be rectangular."

def getWorldFromTextMap(textmap):
    # Converts the programmer-friendly version of a world typed out as ascii
    # characters in a multiline string into a source code-friendly version
    # that lets us access the map as world[x][y].
    worldWidth = len(textmap.strip().split('\n')[0])
    worldHeight = len(textmap.strip().split('\n'))

    textmap = textmap.strip().split('\n')

    world = []
    for i in range(worldWidth):
        world.append([''] * worldHeight)
    for x in range(worldWidth):
        for y in range(worldHeight):
            world[x][y] = textmap[y][x]
    return world


def printWorld(world):
    worldWidth = len(world)
    worldHeight = len(world[0])

    for y in range(worldHeight):
        for x in range(worldWidth):
            sys.stdout.write(world[x][y])
        sys.stdout.write('\n')


def floodFill(world, x, y, oldChar, newChar):
   
    worldWidth = len(world)
    worldHeight = len(world[0])

    if oldChar == None:
        oldChar = world[x][y]

    if world[x][y] != oldChar:
        
        return

    
    world[x][y] = newChar

   
    if x > 0: # left
        floodFill(world, x-1, y, oldChar, newChar)

    if y > 0: # up
        floodFill(world, x, y-1, oldChar, newChar)

    if x < worldWidth-1: # right
        floodFill(world, x+1, y, oldChar, newChar)

    if y < worldHeight-1: # down
        floodFill(world, x, y+1, oldChar, newChar)

def main():
    world = getWorldFromTextMap(textmap)
    printWorld(world)
    print()

    floodFill(world, 5, 8, None, '+')
    printWorld(world)
    print()

    floodFill(world, 0, 0, None, 's')
    printWorld(world)
    print()

if __name__ == '__main__':
    main()
