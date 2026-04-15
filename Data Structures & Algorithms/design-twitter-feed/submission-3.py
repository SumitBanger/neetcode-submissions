class Twitter:

    def __init__(self):
        self.userToTweetsMap = defaultdict(list)
        self.userToFollowersMap = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userToTweetsMap[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []

        userAndFollowerTweets = []
        self.userToFollowersMap[userId].add(userId)
        for followeeId in self.userToFollowersMap[userId]:
            tweetIndex = len(self.userToTweetsMap[followeeId]) - 1
            if tweetIndex >=0:
                timestamp, tweetId = self.userToTweetsMap[followeeId][tweetIndex]
                userAndFollowerTweets.append([timestamp, tweetId, followeeId, tweetIndex])
        heapq.heapify_max(userAndFollowerTweets)

        while len(newsFeed) < 10 and userAndFollowerTweets:
            timestamp, tweetId, followeeId, tweetIndex = heapq.heappop_max(userAndFollowerTweets)
            newsFeed.append(tweetId)
            tweetIndex -= 1
            if tweetIndex >= 0:
                # Get the Next Tweet from the same followee whose tweet got selected for newsFeed
                timestamp, tweetId = self.userToTweetsMap[followeeId][tweetIndex]
                heapq.heappush_max(userAndFollowerTweets, [timestamp, tweetId, followeeId, tweetIndex])


        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowersMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userToFollowersMap[followerId]:
            self.userToFollowersMap[followerId].remove(followeeId)
        
