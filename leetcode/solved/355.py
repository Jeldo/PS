from collections import defaultdict


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follower = defaultdict(set)
        self.tweet = defaultdict(list)  # {user_id: [(tweet_id, time), (...)], ...}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweet[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweets = []
        for t in self.tweet[userId]:
            tweets.append(t)
        for f in self.follower[userId]:
            for t in self.tweet[f]:
                tweets.append(t)
        tweets.sort(key=lambda x: -x[1])
        return [x[0] for x in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
