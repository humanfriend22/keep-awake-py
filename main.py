import sys
from time import sleep
from pyautogui import position, moveTo, Point

# Wait For User to Set Mouse Location
delay = 4

for i in range(delay):
    print('Starting in ' + str(delay - i) + ' seconds')
    sleep(1)

print('\nCalculating Mouse Positions...')

# Calculate Target Positions
starting_pos = position()

target_1 = Point(starting_pos.x + 1, starting_pos.y + 1)
target_2 = Point(starting_pos.x + 2, starting_pos.y + 2)

accepted_positions = {starting_pos, target_1, target_2}

print('Done! Starting Infinite Program Loop\n')

userMovedCounter = 0

# Program
try:
        
    while True:
        current_pos = position()

        userMoved = current_pos not in accepted_positions

        if userMoved:
            userMovedCounter += 1

        if userMovedCounter == 3:
            print('You tried to move the cursor too many times! Exiting...')
            exit(0)

        moveTo(target_1.x, target_1.y)
        sleep(1)
        moveTo(target_2.x, target_2.y)
        sleep(1)
except:
    exit(0)