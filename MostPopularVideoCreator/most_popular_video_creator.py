class Solution:
    def mostPopularCreator(self, creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        import collections

        creator_popularity = collections.defaultdict(int)
        # Stores [max_views_for_creator, lexicographically_smallest_id_for_max_views_at_that_view_count]
        # Initialize with -1 views to ensure any valid view count is greater,
        # and an empty string for ID to ensure any valid ID (lowercase letters) is lexicographically smaller.
        creator_most_viewed_video = collections.defaultdict(lambda: [-1, ""]) 

        n = len(creators)

        for i in range(n):
            creator = creators[i]
            video_id = ids[i]
            view_count = views[i]

            # Update creator popularity
            creator_popularity[creator] += view_count

            # Update most viewed video for this creator
            current_max_views, current_best_id = creator_most_viewed_video[creator]

            if view_count > current_max_views:
                creator_most_viewed_video[creator] = [view_count, video_id]
            elif view_count == current_max_views:
                # If views are same, choose lexicographically smaller ID
                if video_id < current_best_id:
                    creator_most_viewed_video[creator] = [view_count, video_id]
        
        max_popularity = 0
        if creator_popularity: # Check if dictionary is not empty (handles n=0, though constraints say n>=1)
            max_popularity = max(creator_popularity.values())

        result = []
        for creator, popularity in creator_popularity.items():
            if popularity == max_popularity:
                # Retrieve the most viewed video ID for this creator
                # The stored value is [max_views, video_id], we need the video_id (index 1)
                result.append([creator, creator_most_viewed_video[creator][1]])
        
        return result