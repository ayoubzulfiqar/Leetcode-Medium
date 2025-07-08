import collections

class Solution:
    def maximumCaughtPeople(self, tag: list[int], dist: int) -> int:
        uncaught_people_indices = collections.deque()
        caught_pairs = 0

        for i in range(len(tag)):
            if tag[i] == 1:
                # This is a person.
                # Remove people from the left of the deque who are now too far to form a pair with current person 'i'.
                # A person at 'p_idx' is too far if 'i - p_idx > dist'.
                while uncaught_people_indices and uncaught_people_indices[0] < i - dist:
                    uncaught_people_indices.popleft()

                # If there's anyone left in the deque, they can form a pair with person 'i'.
                # We greedily form a pair with the earliest available person (uncaught_people_indices[0]).
                # This leaves later available people for future potential pairings, maximizing the total.
                if uncaught_people_indices:
                    uncaught_people_indices.popleft() # This person is now part of a pair
                    caught_pairs += 1
                else:
                    # No one to form a pair with this person 'i' from the left within 'dist'.
                    # So, 'i' becomes a potential candidate to form a pair with future people.
                    uncaught_people_indices.append(i)
        
        # Each successful pair involves two people.
        return caught_pairs * 2