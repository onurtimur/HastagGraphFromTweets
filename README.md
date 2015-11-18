# HastagGraphFromTweets
Drawing network graph for related hastags from tweets.

This program will run at Python 2.7.x 64-bit distribution.

Dependency:
These packages must be imported in order to use the program:

-networkx
-json
-string
-unicode
-matplotlib
-datetime
-time

It is one python file that divided into functions.There are 5 functions in flow.


generateTags function:

This function reads the tweets.txt file which contains the tweets for the last 60 seconds from all over the world.After importing the tweets there is a loop that goes to each tweets entitiy property and looks if there is any hastag in it, if there is a hasthag thats text is not null ,takes that hashtag.
On the second step it looks to hastag whether it contains any unicode and if so , it cleans the hastag text. and appends it to temporary list. Also second attribute  "created_at" is also imported from tweets to compare the time intervals between each tweet.
So there is a control that looks to each tweet's timestamp and if it is older than 1 minute from the lastest tweet, It won't be used to generate the graph.
Finally hastags will be passed to "getEdgesFromPairs function.

cleanTweets function:

Tweets data is passed from "generateTags" function into this function. Each tweets "text" and "created_at" property is imported and "text" is controlled in order to check if it contains any unicode other than basic-latin. If it contains a unicode character , the corresponding character will be deleted and counter will count each unicode tweet.
Finally cleaned tweets will be written into "ft2.txt" output file with count of each unicode tweet.

getEdgesfromPairs function:

all hastags from "generateTags" is passed into this function to create 2 pairs in order to link each node in the graph.

calc_average_degree function:

Degree of all nodes is divided by the node number in this function. And the result is written into "ft2.txt" output file.

tweetFlow function:

All functions are called in every 60 second loop in the order of:

-generateTags
-getEdgesFromPairs
-calc_average_node

First the nodes of hashtags is imported from tweets , edges is derived from the nodes ,average node degree is calculated and finally the graph is drawed from the inputs.



