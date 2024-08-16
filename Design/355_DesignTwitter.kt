package Design

/**
 * Your Twitter object will be instantiated and called as such:
 * var obj = Twitter()
 * obj.postTweet(userId,tweetId)
 * var param_2 = obj.getNewsFeed(userId)
 * obj.follow(followerId,followeeId)
 * obj.unfollow(followerId,followeeId)
 */

class Twitter() {

    // Pair<IdUser, TweetId>
    private var stackTweets = ArrayList<Pair<Int, Int>>()
    private var followingMap = HashMap<Int, ArrayList<Int>>()

    fun postTweet(userId: Int, tweetId: Int) {
        stackTweets.add(0, Pair(userId, tweetId))

        if (!(followingMap.containsKey(userId))){
            var firstFollowing = ArrayList<Int>()
            firstFollowing.add(userId)
            followingMap.put(userId, firstFollowing)
        }
    }

    fun follow(followerId: Int, followeeId: Int) {

        if (followingMap.containsKey(followerId)){
            var following = followingMap.get(followerId)
          //  print(following)
            following?.add(followeeId)

            followingMap.replace(followerId, following!!)
        } else{
            var entrLevel = ArrayList<Int>()
            entrLevel.add(followerId)
            entrLevel.add(followeeId)
            followingMap.put(followerId, entrLevel)

        }

    }

    fun unfollow(followerId: Int, followeeId: Int) {

        if (followerId != followeeId){
            if (followingMap.containsKey(followerId)){
                followingMap.get(followerId)!!.remove(followeeId)
            }
        }
    }

    fun getNewsFeed(userId: Int): List<Int> {

        var queue = ArrayList<Int>()

        for (i in 0..stackTweets.size-1){
            var currentUser = stackTweets.get(i).first
            if (followingMap.containsKey(userId)){
                if (followingMap.get(userId)!!.contains(currentUser)){
                    queue.add(stackTweets.get(i).second)
                }

            }

            if (queue.size > 9){
                return queue
            }

        }

        return queue
    }

    fun printAlltweets(){

        for (tweet in stackTweets){
            println("userId: ${tweet.first} post: ${tweet.second}")
        }

    }

    fun printFollowingsStructure(){

        for (user in followingMap){
            println("UserId: ${user.key} follow ${user.value}")
        }

    }

}

fun main(){

    /*
    ["Twitter","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
    [[],[1,1],[1],[2,1],[2],[2,1],[2]]

    Expected:
    [null,null,[1],null,[1],null,[]]

    Output:
    [null,null,[1],null,[],null,[]]

     */

    var systemTwitter = Twitter()
    systemTwitter.postTweet(1,1)
    println(systemTwitter.getNewsFeed(1))
    systemTwitter.follow(2,1)
    systemTwitter.postTweet(2,6)
    println(systemTwitter.getNewsFeed(1))
    systemTwitter.unfollow(1,2)
    println(systemTwitter.getNewsFeed(1))
    systemTwitter.printAlltweets()

}