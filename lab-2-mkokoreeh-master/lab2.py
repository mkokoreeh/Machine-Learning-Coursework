# you can add imports, but you should not rely on libraries that are not already provided in "requirements.txt #
import heapq
from heapq import heappush, heappop
from lab2_utils import TextbookStack, apply_sequence
from collections import deque


# Comparator class made so heapq functions can use f(n) to compare Textbook Stacks
class Comparator:
    def __init__(self, cost, stack, sequence):
        self.stack = stack
        self.cost = cost
        self.sequence = sequence

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost


def heuristic(stack):
    heuristic_value = 0

    for idx in range(stack.num_books - 1):
        # If this is the last position, stop checking to avoid out of range errors
        if idx == stack.num_books - 1:
            break
        # Check heuristic factor 1
        if abs(stack.order[idx] - stack.order[idx + 1]) > 1:
            heuristic_value += 1
        # Check heuristic factor 2
        elif stack.orientations[idx] != stack.orientations[idx + 1]:
            heuristic_value += 1
        # Check heuristic factor 3, NOTE: No need to check for adjacency for order since factor 1 handles that case
        elif idx != stack.order[idx] and stack.orientations[idx] == 1 and stack.orientations[idx + 1] == 1:
            heuristic_value += 1
        # Check heuristic factor 4, NOTE: No need to check for adjacency since factor 1 handles it
        elif idx == stack.order[idx] and stack.orientations[idx] == 0 and stack.orientations[idx + 1] == 0:
            heuristic_value += 1

    return heuristic_value


def a_star_search(stack):
    # --- v ADD YOUR CODE HERE v --- #

    flip_sequence = []
    fringe = []
    visited = set()
    # Bin Heap to ensure each time we pop it is the lowest cost stack
    heapq.heappush(fringe, Comparator(0, stack, []))

    while fringe:
        node = heapq.heappop(fringe)
        # Pop the lowest cost stack for expansion
        curr_stack = node.stack
        curr_seq = node.sequence

        if curr_stack.check_ordered():
            return curr_seq

        # Hashing the Textbook Stack by turning the order and orientation into lists and combining them into a tuple
        hash_tuple = (tuple(curr_stack.order.tolist()), tuple(curr_stack.orientations.tolist()))
        if hash_tuple not in visited:
            visited.add(hash_tuple)
            for idx in range(curr_stack.num_books):
                # Loop through every position possible and flip in each spot
                new_node = curr_stack.copy()
                new_node.flip_stack(idx + 1)
                # new cost = distance between parent and source + 1 (for dist. between child + parent) + h(child)
                new_cost = len(curr_seq) + 1 + heuristic(new_node)
                # Keep append the recent flip to the sequences of flips for parents to get path to child
                new_seq = curr_seq + [idx + 1]
                # Push the Comparator class to allow heappush to compare costs and maintain heap property
                heapq.heappush(fringe, Comparator(new_cost, new_node, new_seq))

    return flip_sequence

    # ---------------------------- #


def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #
