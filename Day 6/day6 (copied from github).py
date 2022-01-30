# Day 6 - Lanternfish

# Imports
from collections import defaultdict

# Input Handling
with open('./day6.in') as fin:
    fishes = [int(i) for i in fin.read().strip().split(',')]

# Part 1:
def part1():
    allFish = fishes.copy()
    DAYS = 80

    # Run simulation for 80 days
    while DAYS > 0:
        
        # Check for fishes that have to reproduce
        for fish in range(0, len(allFish)):
            if allFish[fish] == 0:                          # If needs to reproduce
                allFish[fish] = 7                               # Restart its reproduction cycle 
                allFish.append(9)                               # Add the baby to the list
        
        # Decrease all fishes reproduction days by 1
        for fish in range(0, len(allFish)):
            allFish[fish] -= 1

        DAYS -= 1

    return len(allFish)                                     # Find out total fish


# Part 2:
def part2():
    allFish = fishes.copy()
    DAYS = 256

    # Creating map of fish
    fishMap = {}
    for fish in allFish:                            # Travels list of integers
        if fish not in fishMap:                         # Add a (key: value) pair to the dict if key not on yet 
            fishMap[fish] = 0                           # Set that (key: value) pair to (key: 0) intially
        fishMap[fish] += 1                              # Adds 1 to the (key: value) pair, (key: value+1)


    # Change fishes states
    for day in range(DAYS):
        updatedFishMap = defaultdict(int)           # Avoids 'KeyError' by creating a key using the function passed | Creates iterable dict

        # Go to each fish to change its state                                            
        for fish, count in fishMap.items():
            if fish == 0:                           # Take all fishes that need to reproduce
                updatedFishMap[6] += count          # Reset their reproduction date by changing their state
                updatedFishMap[8] += count          # Add all the fishes offspring to the highest state
            else:
                updatedFishMap[fish-1] += count     # Move all fish to the state below theirs

            fishMap = updatedFishMap                # Update the main list
        
    return(sum(fishMap.values()))



print("Answer to part 1: ", part1())
print("Answer to part 2: ", part2())
