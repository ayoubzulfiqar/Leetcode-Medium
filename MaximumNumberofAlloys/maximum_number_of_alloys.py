def maxNumberOfAlloys(n: int, k: int, budget: int, composition: list[list[int]], stock: list[int], cost: list[int]) -> int:
    max_alloys = 0
    
    for machine_idx in range(k):
        low = 0
        high = 2 * 10**8 + 100 
        current_machine_max_alloys = 0
        
        while low <= high:
            mid_alloys = low + (high - low) // 2
            
            cost_required = 0
            
            for metal_type_idx in range(n):
                required_for_metal_type = composition[machine_idx][metal_type_idx] * mid_alloys
                
                needed_to_buy = max(0, required_for_metal_type - stock[metal_type_idx])
                
                cost_for_metal_type = needed_to_buy * cost[metal_type_idx]
                
                cost_required += cost_for_metal_type
                
                if cost_required > budget:
                    break
            
            if cost_required <= budget:
                current_machine_max_alloys = mid_alloys
                low = mid_alloys + 1
            else:
                high = mid_alloys - 1
        
        max_alloys = max(max_alloys, current_machine_max_alloys)
        
    return max_alloys