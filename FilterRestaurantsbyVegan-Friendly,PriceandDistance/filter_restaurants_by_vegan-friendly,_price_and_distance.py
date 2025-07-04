class Solution:
    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
        filtered_restaurants = []
        
        for restaurant in restaurants:
            rid, rating, is_vegan, price, distance = restaurant
            
            if veganFriendly == 1 and is_vegan == 0:
                continue
            
            if price > maxPrice:
                continue
            
            if distance > maxDistance:
                continue
            
            filtered_restaurants.append([rating, rid])
            
        filtered_restaurants.sort(key=lambda x: (-x[0], -x[1]))
        
        result_ids = [res[1] for res in filtered_restaurants]
        
        return result_ids