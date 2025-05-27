# Reeborg Maze Solver - Right-Hand Rule Algorithm
# Angela Yu 100 Days of Code - Day 6
# Lost in a Maze Challenge

# ============================================================================
# HELPER FUNCTION
# ============================================================================

def turn_right():
    """
    Turn Reeborg right by turning left three times.
    Since Reeborg only has turn_left() function, we simulate turn_right()
    by using the fact that 3 left turns = 1 right turn (270° left = 90° right)
    """
    turn_left()  # First left turn (90°)
    turn_left()  # Second left turn (180°)
    turn_left()  # Third left turn (270° = 90° right)

# ============================================================================
# INITIAL POSITIONING
# ============================================================================

# Move forward until hitting a wall to position Reeborg at maze entrance
while front_is_clear():
    move()

# Turn left to face into the maze properly
turn_left()

# ============================================================================
# MAIN MAZE SOLVING ALGORITHM - RIGHT-HAND RULE
# ============================================================================

# Continue until Reeborg reaches the goal (flag)
while not at_goal():
    
    # PRIORITY 1: Always try to turn right first
    # This keeps Reeborg's "right hand" on the wall
    if right_is_clear():
        turn_right()  # Turn right using our custom function
        move()        # Move forward into the right passage
    
    # PRIORITY 2: If can't turn right, go straight ahead
    # This continues following the wall when right is blocked
    elif front_is_clear():
        move()        # Move forward in current direction
    
    # PRIORITY 3: If both right and front are blocked, turn left
    # This handles corners and dead ends by rotating until path is found
    else:
        turn_left()   # Turn left to find new direction
        # Note: We don't move after turning left - we re-evaluate in next loop

# ============================================================================
# ALGORITHM EXPLANATION
# ============================================================================
"""
The Right-Hand Rule (Wall-Following Algorithm):

1. Imagine keeping your right hand on the wall at all times
2. Always try to turn right when possible (follow the wall)
3. If right is blocked, go straight (continue along wall)
4. If both right and front blocked, turn left (navigate around corner)

This algorithm guarantees finding the exit in any simply-connected maze
(a maze where all walls are connected and there are no isolated wall pieces).

The algorithm works because:
- It systematically explores the maze boundary
- It never gets lost since it always follows a consistent rule
- It eventually traces around the entire accessible area until finding the goal

Time Complexity: O(n) where n is the number of cells in the maze
Space Complexity: O(1) - no memory of previous positions needed
"""
