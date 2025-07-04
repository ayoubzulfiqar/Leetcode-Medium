def dot_product_sparse(v1: dict, v2: dict) -> int:
    dot_product = 0
    
    if len(v1) > len(v2):
        v1, v2 = v2, v1
        
    for index, value1 in v1.items():
        if index in v2:
            dot_product += value1 * v2[index]
            
    return dot_product