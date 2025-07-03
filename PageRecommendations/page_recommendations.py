class PageRecommender:
    def __init__(self):
        self.pages = {}

    def add_page(self, page_id, keywords):
        """
        Adds a page to the recommender system with its associated keywords.

        Args:
            page_id (str): A unique identifier for the page.
            keywords (list[str]): A list of keywords/tags describing the page content.
        """
        self.pages[page_id] = set(keywords)

    def get_recommendations(self, target_page_id, num_recommendations=5):
        """
        Generates page recommendations for a given target page based on shared keywords.

        Args:
            target_page_id (str): The ID of the page for which to find recommendations.
            num_recommendations (int): The maximum number of recommendations to return.

        Returns:
            list[str]: A list of page IDs recommended for the target page,
                       sorted by the number of shared keywords in descending order.
                       Returns an empty list if the target page does not exist
                       or has no keywords.
        """
        if target_page_id not in self.pages:
            return []

        target_keywords = self.pages[target_page_id]
        if not target_keywords:
            return []

        recommendation_scores = [] # Stores (page_id, common_keywords_count)

        for page_id, keywords in self.pages.items():
            if page_id == target_page_id:
                continue # Do not recommend the page itself

            if not keywords:
                continue # Cannot score similarity if candidate has no keywords

            # Calculate similarity based on the number of common keywords
            common_keywords_count = len(target_keywords.intersection(keywords))
            
            if common_keywords_count > 0:
                recommendation_scores.append((page_id, common_keywords_count))

        # Sort recommendations by score (number of common keywords) in descending order
        recommendation_scores.sort(key=lambda x: x[1], reverse=True)

        # Extract page IDs and return the top N recommendations
        recommended_page_ids = [page_id for page_id, score in recommendation_scores]
        return recommended_page_ids[:num_recommendations]

if __name__ == "__main__":
    recommender = PageRecommender()

    # Add example pages with their keywords
    recommender.add_page("page_101", ["python", "programming", "tutorial", "beginner"])
    recommender.add_page("page_102", ["java", "programming", "oop", "advanced"])
    recommender.add_page("page_103", ["python", "data_science", "machine_learning", "beginner"])
    recommender.add_page("page_104", ["web_dev", "javascript", "frontend", "tutorial"])
    recommender.add_page("page_105", ["python", "programming", "web_dev", "flask"])
    recommender.add_page("page_106", ["java", "spring", "backend", "advanced"])
    recommender.add_page("page_107", ["data_science", "statistics", "r_language"])
    recommender.add_page("page_108", ["machine_learning", "deep_learning", "neural_networks"])
    recommender.add_page("page_109", ["tutorial", "beginner", "linux", "command_line"])
    recommender.add_page("page_110", ["programming", "algorithms", "data_structures", "java"])
    recommender.add_page("page_111", ["ai", "machine_learning", "ethics"])
    recommender.add_page("page_112", ["cloud", "aws", "devops"])
    recommender.add_page("page_113", ["python", "testing", "pytest"])
    recommender.add_page("page_114", []) # Page with no keywords

    # Get recommendations for various pages
    print("Recommendations for 'page_101' (Python Programming Tutorial):")
    recs_101 = recommender.get_recommendations("page_101", num_recommendations=3)
    for rec in recs_101:
        print(f"- {rec}")

    print("\nRecommendations for 'page_103' (Python Data Science):")
    recs_103 = recommender.get_recommendations("page_103", num_recommendations=4)
    for rec in recs_103:
        print(f"- {rec}")

    print("\nRecommendations for 'page_104' (Web Development Tutorial):")
    recs_104 = recommender.get_recommendations("page_104", num_recommendations=2)
    for rec in recs_104:
        print(f"- {rec}")

    print("\nRecommendations for 'page_102' (Java Advanced Programming):")
    recs_102 = recommender.get_recommendations("page_102", num_recommendations=3)
    for rec in recs_102:
        print(f"- {rec}")

    print("\nRecommendations for 'page_108' (Machine Learning):")
    recs_108 = recommender.get_recommendations("page_108", num_recommendations=2)
    for rec in recs_108:
        print(f"- {rec}")

    print("\nRecommendations for 'non_existent_page':")
    recs_non_existent = recommender.get_recommendations("non_existent_page")
    print(f"- {recs_non_existent}")

    print("\nRecommendations for 'page_114' (Page with no keywords):")
    recs_empty_keywords = recommender.get_recommendations("page_114")
    print(f"- {recs_empty_keywords}")