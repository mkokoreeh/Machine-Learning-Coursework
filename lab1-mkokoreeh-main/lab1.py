# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
import queue
from collections import deque


def breadth_first_search(stack):
    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    visited = [stack]
    bfs = deque()
    bfs.append(stack)
    sequences = deque()
    curr_seq = []
    while bfs:
        node = bfs.popleft()  # - remove source from queue and copy it to process - #
        if sequences:
            curr_seq = sequences.popleft()
        if node not in visited:
            visited.append(node)  # - removed node is now "visited" so we can avoid repeat orientations - #
            if node.check_ordered():
                flip_sequence = curr_seq
                return flip_sequence

        for i in range(node.num_books):  # - add all possible flips from node into queue if it has not yet been visited - #
            child = node.copy()
            child.flip_stack(i+1)

            if child not in visited:  # - add sequences at the same time so that a child is checked at the same time as its sequence - #
                bfs.append(child)
                new_seq = curr_seq + [i+1]  # - appends new flip to associated sequence
                sequences.append(new_seq)

    return flip_sequence
    # ---------------------------- #


def depth_first_search(stack):
    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    visited = [stack]
    dfs = [stack]
    sequences = []
    while dfs:  # - Loop while stack has nodes to check - #
        temp = dfs.pop()  # - pop the node we are checking out of the stack and add its position number to the sequence - #
        node = temp.copy()
        if sequences:
            flip_sequence.append(sequences.pop())

        if node.check_ordered():  # - check if node is correct, if it is, stop searching - #
            return flip_sequence

        if node not in visited:
            visited.append(node)  # - popped node is now "visited" so we can avoid repeat orientations - #

        for i in range(node.num_books):  # - add all possible flips from node into stack if it has not yet been visited - #
            child = node.copy()
            child.flip_stack(i+1)
            if child not in visited:
                dfs.append(child)
                sequences.append(i+1)

    return flip_sequence
    # ---------------------------- #
