# HashtagGraphFromTweets
Drawing network graph for related hashtags from tweets.

This program will run at Python 2.7.x 64-bit distribution. 
Dependency: These packages below must be imported in order to use the program,

•	Networkx
•	json
•	string 
•	unicode 
•	matplotlib 
•	datetime 
•	time

In order to run matplotlib properly some linux distributions should install 

•	libpng-dev
•	libjpeg8-dev
•	libfreetype6-dev 

by entering below command into terminal:

sudo apt-get install libpng-dev libjpeg8-dev libfreetype6-dev

Program runs with python file that divided into several functions.There are 5 functions in the flow. 

Functions

generate_tags function:

This function reads the tweets.txt file which contains the tweets for the last 60 seconds from all over the world.
After importing the tweets there is a loop that goes to each tweets entitiy property and looks if there is any hastag in it,
if there is a hashtag thats text is not null ,takes that hashtag. On the second step it looks to hashtag whether it contains
any unicode and if so , it cleans the hashtag text. and appends it to temporary list. Also second attribute "created_at" is
also imported from tweets to compare the time intervals between each tweet. So there is a control that looks to each tweet's
timestamp and if it is older than 1 minute from the lastest tweet, It won't be used to generate the graph. Finally hashtags
will be passed to "get_edges_from_pairs” function.

clean_tweets function:

Tweets data is passed from "generate_tags" function into this function. Each tweets "text" and "created_at" property is
imported and "text" is controlled in order to check if it contains any unicode other than basic-latin. If it contains a
unicode character , the corresponding character will be deleted and counter will count each unicode tweet. Finally cleaned
tweets will be written into "ft2.txt" output file with count of each unicode tweet.

get_edges_from_pairs function:

Hashtags from "generate_tags" is passed into this function to create 2 pairs in order to link each node in the graph.
calc_average_degree function:
Degree of all nodes is divided by the node number in this function. And the result is written into "ft2.txt" output file.

tweet_flow function:

All functions are called in every 60 second loop in the order of:

•	generate_tags 
•	get_edges_from_pairs 
•	calc_average_node

First the nodes of hashtags are imported from tweets ,then the edges are derived from the nodes ,average node degree is
calculated and finally the graph is drawed from the inputs.


