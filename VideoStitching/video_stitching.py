class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        clips.sort()

        num_clips = 0
        current_reach = 0
        clip_idx = 0

        while current_reach < time:
            next_max_reach = current_reach
            
            while clip_idx < len(clips) and clips[clip_idx][0] <= current_reach:
                next_max_reach = max(next_max_reach, clips[clip_idx][1])
                clip_idx += 1
            
            if next_max_reach == current_reach:
                return -1
            
            current_reach = next_max_reach
            num_clips += 1
            
        return num_clips