class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        low = 0
        high = n - 1
        h_index = 0

        while low <= high:
            mid = low + (high - low) // 2
            
            # 'num_papers_at_least_citations_mid' represents the count of papers
            # whose citation count is at least citations[mid].
            # Since the array is sorted in non-descending order, these are
            # the papers from index 'mid' to 'n-1'. The count is n - mid.
            num_papers_at_least_citations_mid = n - mid
            
            # If the citation count of the paper at 'mid' (citations[mid]) is
            # greater than or equal to the number of papers that have at least
            # citations[mid] citations (num_papers_at_least_citations_mid),
            # then 'num_papers_at_least_citations_mid' is a valid h-index candidate.
            # We want the maximum such h-index, so we store this value and
            # try to find a potentially larger one by looking at papers with
            # higher citation counts (which means moving to smaller indices in
            # the sorted array, i.e., high = mid - 1).
            if citations[mid] >= num_papers_at_least_citations_mid:
                h_index = num_papers_at_least_citations_mid
                high = mid - 1
            else:
                # If citations[mid] is too small for 'num_papers_at_least_citations_mid'
                # papers to qualify (i.e., citations[mid] < num_papers_at_least_citations_mid),
                # then we need to reduce the number of papers considered or find papers
                # with higher citations. This means moving our 'mid' pointer to the right
                # (increasing 'mid'), which will decrease 'num_papers_at_least_citations_mid'
                # and potentially increase citations[mid].
                low = mid + 1
                
        return h_index