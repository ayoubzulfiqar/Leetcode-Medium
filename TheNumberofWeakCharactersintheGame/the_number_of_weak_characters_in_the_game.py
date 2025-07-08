class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        
        weak_characters_count = 0
        max_defense_seen = 0
        
        for attack, defense in properties:
            if defense < max_defense_seen:
                weak_characters_count += 1
            else:
                max_defense_seen = defense
                
        return weak_characters_count