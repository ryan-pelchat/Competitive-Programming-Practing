/*
Problem Title: Design Twitter
Platform: LeetCode
Problem URL: https://leetcode.com/problems/design-twitter/
Difficulty: Medium 
Category: Heap (Priority Queue)

Driver: Ben
Navigator: Ryan
Date Solved: July 9th 2025
Language: C++

Problem Summary:

Implement a class that has features: make a tweet, follow and unfollow account, and show 10 most recent tweets from you or your followers.

Approach:

For each user store their tweets and who they are following. To access newsfeed of a given user aggregate the 10 last tweets of everyone their following into a heap and pop the 10 most recent tweets from the heap. Every tweet is attached to a number which says what number tweet it was chronologically using a counter.

Time Complexity: 0(#numberOfFollowers *  log(#numberOfFollowers))
Space Complexity: 0(#ofTotalTweets + #ofFollowersandFollowees)

Notes:
*/

class Twitter {
public:
    unordered_map<int, vector<pair<int,int>>> tweets;
    unordered_map<int, unordered_set<int>> following;
    int counter;
    Twitter() {
        counter=0;
    }
    
    void postTweet(int userId, int tweetId) {
        tweets[userId].push_back(make_pair(counter,tweetId));
        counter++;
        if (tweets[userId].size()>10){
            tweets[userId].erase(tweets[userId].begin());
        }
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<pair<int,int>> heap;
        int count=0;
        for (auto & i : following[userId]){
            for (auto & j : tweets[i]){
                heap.push_back(j);
            }
        }
        for (auto & j : tweets[userId]){
            heap.push_back(j);
        }
        vector<int> feed;
        int runningCount=0;
        make_heap(heap.begin(), heap.end());
        while(!heap.empty() && runningCount < 10){
            feed.push_back(heap.front().second);
            pop_heap(heap.begin(), heap.end());
            heap.pop_back();
            runningCount++;
        }
        return feed;
    }
    
    void follow(int followerId, int followeeId) {
        following[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        following[followerId].erase(followeeId);
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */