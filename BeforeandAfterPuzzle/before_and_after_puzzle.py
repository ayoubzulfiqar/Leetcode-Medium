import collections

def solve_before_and_after(phrases: list[str]) -> list[str]:
    last_word_map = collections.defaultdict(list)
    first_word_map = collections.defaultdict(list)

    for phrase in phrases:
        words = phrase.split()
        if not words:
            continue
        
        first_word = words[0]
        last_word = words[-1]
        
        last_word_map[last_word].append(phrase)
        first_word_map[first_word].append(phrase)

    connecting_words_set = set()

    for last_w, phrases_ending_with_last_w in last_word_map.items():
        if last_w in first_word_map:
            phrases_starting_with_last_w = first_word_map[last_w]
            
            found_distinct_pair = False
            for p_end in phrases_ending_with_last_w:
                for p_start in phrases_starting_with_last_w:
                    if p_end != p_start:
                        found_distinct_pair = True
                        break
                if found_distinct_pair:
                    break
            
            if found_distinct_pair:
                connecting_words_set.add(last_w)
                
    return list(connecting_words_set)