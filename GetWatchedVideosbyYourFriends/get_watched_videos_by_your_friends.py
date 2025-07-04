import collections

class Solution:
    def watchedVideosByFriends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        
        queue = collections.deque([(id, 0)])
        visited = {id}
        people_at_target_level = []

        while queue:
            current_person, current_level = queue.popleft()

            if current_level == level:
                people_at_target_level.append(current_person)
                continue # Do not explore friends of people already at the target level

            if current_level < level:
                for neighbor in friends[current_person]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_level + 1))
        
        video_frequencies = collections.Counter()
        for person_id in people_at_target_level:
            for video in watchedVideos[person_id]:
                video_frequencies[video] += 1
        
        sorted_videos = sorted(video_frequencies.items(), key=lambda item: (item[1], item[0]))
        
        return [video for video, count in sorted_videos]