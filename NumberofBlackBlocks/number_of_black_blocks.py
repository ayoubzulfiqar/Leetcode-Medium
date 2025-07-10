import collections

class Solution:
    def numberOfBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        block_black_counts = collections.defaultdict(int)

        for r, c in coordinates:
            # A black cell [r, c] can be part of up to four 2x2 blocks.
            # These blocks have top-left corners:
            # [r, c] (if [r, c] is the top-left cell of the block)
            # [r, c-1] (if [r, c] is the top-right cell of the block)
            # [r-1, c] (if [r, c] is the bottom-left cell of the block)
            # [r-1, c-1] (if [r, c] is the bottom-right cell of the block)

            # Iterate through the 4 potential top-left corner offsets (dr, dc)
            # relative to the black cell [r, c].
            # (dr, dc) represents the position of [r, c] within a 2x2 block.
            # (0,0) means [r,c] is top-left, so block top-left is [r,c]
            # (0,1) means [r,c] is top-right, so block top-left is [r,c-1]
            # (1,0) means [r,c] is bottom-left, so block top-left is [r-1,c]
            # (1,1) means [r,c] is bottom-right, so block top-left is [r-1,c-1]
            for dr in range(2):
                for dc in range(2):
                    # Calculate the top-left corner (x, y) of the potential block
                    x = r - dr
                    y = c - dc

                    # Check if (x, y) is a valid top-left corner for a 2x2 block
                    # A valid top-left corner [x, y] must satisfy:
                    # 0 <= x < m - 1 (to ensure [x+1, y] is within bounds)
                    # 0 <= y < n - 1 (to ensure [x, y+1] is within bounds)
                    if 0 <= x < m - 1 and 0 <= y < n - 1:
                        block_black_counts[(x, y)] += 1
        
        arr = [0] * 5

        # Populate arr[1] through arr[4] based on the counts in block_black_counts
        for count in block_black_counts.values():
            arr[count] += 1
        
        # Calculate arr[0], the number of blocks with zero black cells.
        # Total number of possible 2x2 blocks in the grid.
        total_blocks = (m - 1) * (n - 1)
        
        # Sum of blocks that have at least one black cell (i.e., those counted in block_black_counts).
        # This is the sum of arr[1], arr[2], arr[3], and arr[4].
        blocks_with_black_cells = sum(arr[1:])

        # The number of blocks with zero black cells is the total blocks
        # minus the blocks that contain at least one black cell.
        arr[0] = total_blocks - blocks_with_black_cells

        return arr