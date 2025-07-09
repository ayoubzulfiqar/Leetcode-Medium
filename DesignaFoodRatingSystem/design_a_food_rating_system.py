import collections
import heapq

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        # Stores food_name -> [cuisine, rating]
        self.food_details = {}
        
        # Stores cuisine -> min-heap of (-rating, food_name)
        # Using min-heap with negative ratings to simulate max-heap for ratings
        # and food_name for lexicographical tie-breaking
        self.cuisine_ratings = collections.defaultdict(list)
        
        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]
            
            self.food_details[food] = [cuisine, rating]
            heapq.heappush(self.cuisine_ratings[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        # Get the cuisine for the food
        cuisine = self.food_details[food][0]
        
        # Update the rating in food_details
        self.food_details[food][1] = newRating
        
        # Add the new rating to the heap for its cuisine.
        # The old entry for this food in the heap becomes "stale"
        # and will be filtered out by highestRated when encountered.
        heapq.heappush(self.cuisine_ratings[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # Get the min-heap for the given cuisine
        heap = self.cuisine_ratings[cuisine]
        
        while True:
            # Peek at the top element of the heap
            neg_rating, food_name = heap[0]
            
            # Get the current actual rating for this food from food_details
            current_actual_rating = self.food_details[food_name][1]
            
            # Check if the heap entry is still valid (not stale)
            if neg_rating == -current_actual_rating:
                # This entry is valid and represents the highest-rated food (or tied highest)
                # with the smallest lexicographical name.
                return food_name
            else:
                # This entry is stale (its rating has changed since it was added to the heap).
                # Pop it and continue checking the next element in the heap.
                heapq.heappop(heap)