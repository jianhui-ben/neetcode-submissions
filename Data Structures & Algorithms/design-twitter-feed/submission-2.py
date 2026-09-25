import heapq
class Twitter:

    def __init__(self):
        """
        we need 
        1. user_post_tweets_map on {userId: [(cur_time1, tweetId1), (cur_time2, tweetId2) ...]}
        2. follower_map on {follower1: set(followee1, followee2) ...} 
        postTweet (O1): 
        update user_tweets_map

        follow / unfollow (less frequent operation):  O(1)

        getNewsFeed (nlogn): just fetch from user_tweets_feed_map
        """
        self.user_tweets_map = defaultdict(list)
        self.follower_followees_map = defaultdict(set)
        self.cur_time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets_map[userId].append((self.cur_time, tweetId))
        self.cur_time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follower_followees_map[userId].add(userId)
        max_heap = []
        
        for followee in self.follower_followees_map[userId]:
            tweets = self.user_tweets_map[followee]
            if tweets:
                post_time, tweetId = tweets[-1]
                max_heap.append((-post_time, tweetId, followee, len(tweets) - 2))
        heapq.heapify(max_heap)

        out = []
        while max_heap and len(out) < 10:
            _, tweetId, followee, next_idx = heapq.heappop(max_heap)
            out.append(tweetId)
            if next_idx >= 0:
                tweets = self.user_tweets_map[followee]
                post_time, tweetId = tweets[next_idx]
                heapq.heappush(max_heap, (-post_time, tweetId, followee, next_idx - 1))
        return out
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_followees_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_followees_map[followerId]:
            self.follower_followees_map[followerId].remove(followeeId)
