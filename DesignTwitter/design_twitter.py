import collections

class Twitter:

    def __init__(self):
        self.tweets = []
        self.followers = collections.defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets.append((self.timestamp, userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        news_feed = []
        
        followed_and_self = self.followers[userId].copy()
        followed_and_self.add(userId)

        for i in range(len(self.tweets) - 1, -1, -1):
            timestamp, poster_id, tweet_id = self.tweets[i]
            if poster_id in followed_and_self:
                news_feed.append(tweet_id)
                if len(news_feed) == 10:
                    break
        
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)