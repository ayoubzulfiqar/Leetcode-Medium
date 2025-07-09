def calculate_rank_changes(initial_rankings, final_rankings):
    item_to_initial_rank = {item: rank for rank, item in enumerate(initial_rankings)}

    improved_count = 0
    declined_count = 0
    same_count = 0

    for final_rank, item in enumerate(final_rankings):
        initial_rank = item_to_initial_rank[item]

        if final_rank < initial_rank:
            improved_count += 1
        elif final_rank > initial_rank:
            declined_count += 1
        else:
            same_count += 1
            
    return improved_count, declined_count, same_count

if __name__ == '__main__':
    initial_rankings_sample_1 = ["USA", "China", "India", "Germany"]
    final_rankings_sample_1 = ["China", "USA", "Germany", "India"]
    
    print(calculate_rank_changes(initial_rankings_sample_1, final_rankings_sample_1))

    initial_rankings_sample_2 = ["A", "B", "C"]
    final_rankings_sample_2 = ["A", "C", "B"]
    print(calculate_rank_changes(initial_rankings_sample_2, final_rankings_sample_2))

    initial_rankings_sample_3 = ["X", "Y", "Z"]
    final_rankings_sample_3 = ["X", "Y", "Z"]
    print(calculate_rank_changes(initial_rankings_sample_3, final_rankings_sample_3))