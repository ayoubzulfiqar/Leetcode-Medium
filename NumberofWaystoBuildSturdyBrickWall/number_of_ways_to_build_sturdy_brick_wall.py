def buildWall(height: int, width: int, bricks: list[int]) -> int:
    bricks_set = set(bricks)
    
    valid_layer_masks = []
    
    def find_layer_configurations(current_width, current_mask):
        if current_width == width:
            valid_layer_masks.append(current_mask)
            return
        
        if current_width > width:
            return
            
        for brick_len in bricks_set:
            if current_width + brick_len <= width:
                new_mask = current_mask
                if current_width + brick_len < width:
                    new_mask |= (1 << (current_width + brick_len - 1))
                
                find_layer_configurations(current_width + brick_len, new_mask)

    find_layer_configurations(0, 0)
    
    valid_layer_masks = sorted(list(set(valid_layer_masks)))
    
    if not valid_layer_masks:
        return 0

    num_masks = len(valid_layer_masks)
    
    dp_prev_layer = [1] * num_masks
    
    for h in range(2, height + 1):
        dp_current_layer = [0] * num_masks
        
        for current_mask_idx in range(num_masks):
            current_mask = valid_layer_masks[current_mask_idx]
            
            for prev_mask_idx in range(num_masks):
                prev_mask = valid_layer_masks[prev_mask_idx]
                
                if (current_mask & prev_mask) == 0:
                    dp_current_layer[current_mask_idx] += dp_prev_layer[prev_mask_idx]
        
        dp_prev_layer = dp_current_layer
    
    total_ways = sum(dp_prev_layer)
    
    return total_ways