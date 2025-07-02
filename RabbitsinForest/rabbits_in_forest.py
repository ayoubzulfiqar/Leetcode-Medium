import collections

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        counts = collections.Counter(answers)
        total_rabbits = 0
        for answer_val, num_rabbits_reporting_this_answer in counts.items():
            group_size = answer_val + 1
            
            # Calculate the number of full groups required for rabbits reporting this answer.
            # This is equivalent to ceil(num_rabbits_reporting_this_answer / group_size)
            # Using integer division: (numerator + denominator - 1) // denominator
            num_groups_needed = (num_rabbits_reporting_this_answer + group_size - 1) // group_size
            
            # Each group contains 'group_size' rabbits.
            total_rabbits += num_groups_needed * group_size
            
        return total_rabbits