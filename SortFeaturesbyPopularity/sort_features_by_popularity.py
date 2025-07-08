import collections
import re

class Solution:
    def sortFeatures(self, features: list[str], reviews: list[str]) -> list[str]:
        feature_popularity = collections.defaultdict(int)
        
        for review in reviews:
            words_in_review_set = set(re.findall(r'\b\w+\b', review.lower()))
            
            for feature_original_casing in features:
                feature_lower = feature_original_casing.lower()
                
                if feature_lower in words_in_review_set:
                    feature_popularity[feature_original_casing] += 1
        
        features_with_popularity = []
        for feature in features:
            features_with_popularity.append((feature, feature_popularity[feature]))
            
        features_with_popularity.sort(key=lambda x: (-x[1], x[0]))
        
        sorted_features = [feature for feature, count in features_with_popularity]
        
        return sorted_features