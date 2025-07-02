class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_length = 0
        # current_path_lengths[depth] stores the length of the path
        # up to the directory at (depth-1), including the '/' separator
        # that would precede an item at 'depth'.
        # For example, if "dir" is at depth 0, current_path_lengths[1] will store len("dir/")
        # current_path_lengths[0] is 0, representing the path before any root element.
        current_path_lengths = {0: 0} 

        for line in input.split('\n'):
            # Determine the depth by counting leading tabs
            depth = line.count('\t')
            
            # Extract the name (remove leading tabs)
            name = line.lstrip('\t')

            # Check if it's a file (contains a dot)
            if '.' in name:
                # Calculate the absolute path length for this file
                # It's the length of the path to its parent directory (current_path_lengths[depth])
                # plus the length of the file name itself.
                absolute_file_path_length = current_path_lengths[depth] + len(name)
                
                # Update the maximum length found so far
                max_length = max(max_length, absolute_file_path_length)
            else:
                # It's a directory
                # Store the length of the path to this directory, including its name
                # and the '/' separator for any potential children.
                # This length will be used for items at depth + 1.
                current_path_lengths[depth + 1] = current_path_lengths[depth] + len(name) + 1
        
        return max_length