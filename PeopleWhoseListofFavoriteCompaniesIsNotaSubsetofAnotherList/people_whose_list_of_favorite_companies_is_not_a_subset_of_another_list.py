class Solution:
    def peopleWhoseListOfFavoriteCompaniesIsNotASubsetOfAnotherList(self, favoriteCompanies: list[list[str]]) -> list[int]:
        n = len(favoriteCompanies)
        
        # Convert each list of companies to a set for efficient subset checking
        favorite_sets = [set(companies) for companies in favoriteCompanies]
        
        result_indices = []
        
        # Iterate through each person
        for i in range(n):
            is_not_subset_of_any_other = True
            
            # Compare person i's list with every other person j's list
            for j in range(n):
                if i == j:
                    continue  # Skip comparing with self
                
                # Check if person i's list is a subset of person j's list
                if favorite_sets[i].issubset(favorite_sets[j]):
                    is_not_subset_of_any_other = False
                    break  # Found a superset, no need to check further for this person i
            
            # If person i's list was not a subset of any other list, add their index to the result
            if is_not_subset_of_any_other:
                result_indices.append(i)
                
        # The indices are naturally added in increasing order by the loop
        return result_indices