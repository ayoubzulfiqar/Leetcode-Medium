import collections

class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        counts = collections.Counter(barcodes)
        
        # Sort items by frequency in descending order.
        # This ensures that the most frequent barcodes are placed first,
        # maximizing the distance between their occurrences.
        sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        
        n = len(barcodes)
        result = [0] * n
        
        # Initialize index for placing elements.
        # We'll fill even indices first, then odd indices.
        idx = 0 
        
        for barcode, count in sorted_items:
            # Place the current barcode 'count' times
            for _ in range(count):
                result[idx] = barcode
                idx += 2 # Move to the next available position, skipping one
                
                # If we have reached or exceeded the end of the array by filling even positions,
                # switch to filling odd positions starting from index 1.
                if idx >= n:
                    idx = 1 
                    
        return result