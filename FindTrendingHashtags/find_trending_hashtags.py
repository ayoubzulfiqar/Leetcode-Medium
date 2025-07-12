import re
from collections import Counter

def find_trending_hashtags(posts: list[str], top_n: int = None) -> list[tuple[str, int]]:
    """
    Finds trending hashtags from a list of text posts.

    Args:
        posts: A list of strings, where each string represents a post.
        top_n: An optional integer specifying the number of top trending hashtags to return.
               If None, all unique hashtags sorted by frequency are returned.

    Returns:
        A list of tuples, where each tuple contains a hashtag (string) and its count (int).
        The list is sorted in descending order of counts. For ties in counts, hashtags
        are sorted alphabetically (case-insensitive as hashtags are normalized to lowercase).
    """
    hashtag_counts = Counter()
    # Regex to find words starting with '#'
    # \w+ matches one or more word characters (alphanumeric + underscore)
    hashtag_pattern = re.compile(r'#\w+')

    for post in posts:
        # Find all hashtags in the post
        found_hashtags = hashtag_pattern.findall(post)
        for hashtag in found_hashtags:
            # Normalize hashtag to lowercase for consistent counting
            hashtag_counts[hashtag.lower()] += 1

    # Sort the hashtags:
    # 1. By count in descending order (-item[1])
    # 2. By hashtag name in ascending alphabetical order (item[0]) for tie-breaking
    sorted_hashtags = sorted(
        hashtag_counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    if top_n is not None:
        return sorted_hashtags[:top_n]
    else:
        return sorted_hashtags

if __name__ == "__main__":
    example_posts = [
        "Loving this #Python tutorial!",
        "Learning #Python and #DataScience is fun.",
        "Just finished a great #MachineLearning course.",
        "Exploring #DataScience tools.",
        "Another day, another #Python script.",
        "Check out #AI and #ML!",
        "More #AI for everyone.",
        "A new #python course is out."
    ]

    # Find top 3 trending hashtags
    trending_top_3 = find_trending_hashtags(example_posts, top_n=3)
    print(trending_top_3)

    # Find all trending hashtags
    all_trending = find_trending_hashtags(example_posts)
    print(all_trending)

    # Example with no hashtags
    no_hashtags_posts = [
        "Hello world",
        "This is a test"
    ]
    trending_none = find_trending_hashtags(no_hashtags_posts)
    print(trending_none)

    # Example with empty list
    empty_posts = []
    trending_empty = find_trending_hashtags(empty_posts)
    print(trending_empty)