import collections
import bisect

class TweetCounts:

    def __init__(self):
        self.tweets = collections.defaultdict(list)
        
        self.freq_map = {
            "minute": 60,
            "hour": 3600,
            "day": 86400
        }

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort_left(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list[int]:
        chunk_size = self.freq_map[freq]
        
        tweet_times = self.tweets[tweetName]
        
        results = []
        current_chunk_start = startTime
        
        while current_chunk_start <= endTime:
            current_chunk_end = min(current_chunk_start + chunk_size - 1, endTime)
            
            left_idx = bisect.bisect_left(tweet_times, current_chunk_start)
            right_idx = bisect.bisect_right(tweet_times, current_chunk_end)
            
            results.append(right_idx - left_idx)
            
            current_chunk_start = current_chunk_end + 1
            
        return results