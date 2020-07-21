
def can_reach_end(A):
    # Next positions available
    nextPos = []
    # Farthest we have reached yet
    maxReach = 0
    if len(A) == 0:
        return False

    # Start at start
    nextPos.append(0)

    while len(nextPos) > 0:
        # If we reached the end, return True
        if maxReach >= len(A) - 1:
            return True

        curr_pos = nextPos.pop(0)
        if A[curr_pos] == 0:
            continue

        # Update maxReach
        curr_reach = curr_pos + A[curr_pos]
        maxReach = max(maxReach, curr_reach)

        [nextPos.append(curr_pos + k) for k in range(1, A[curr_pos]+1) if (curr_pos + k) not in nextPos]

    return False





if __name__ == '__main__':

    print(can_reach_end([3,2,0,1,2,0,1]))