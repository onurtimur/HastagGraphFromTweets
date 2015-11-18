import datetime
import time
from pprint import pprint
import os
import json
import string
import networkx as nx
import matplotlib.pyplot as plt



def clean_tweets(data,listlen):
    global file_dir
    tweet_collector = ""
    unicode_counter = 0
    try:
        for i in range(listlen):
            text = data[i]['text']
            created_at = data[i]['created_at']

            try:
                text.decode('utf-8')

            except UnicodeError:

                unicode_counter +=1
                for letter in text:
                    if letter not in string.ascii_letters:
                        text = text.replace(letter,"")

            tweet_collector += "\n" + text + "\t" + "timestamp: " + created_at

    except KeyError:
        pass

    tweet_collector += "\n" + str(unicode_counter) + " tweets contained unicode."

    with open(file_dir + 'tweet_output/ft1.txt', "w") as text_file:
        text_file.write(tweet_collector)
    text_file.close()

def genereate_tags():
    global latest
    global tinterval
    global graph
    global file_dir
    f = open(file_dir + 'tweet_input/tweets.txt')
    tivitler = f.read()
    f.close()
    data = [json.loads(str(item)) for item in tivitler.strip().split('\n')]
    listlen = len(data)
    templist=[]
    pairs = []

    clean_tweets(data,listlen)
    for i in range(listlen):

        try:
            hashtags = data[i]['entities']['hashtags']
            created_at = data[i]['created_at']

            if isinstance(hashtags, list):
                for hast in hashtags:
                    if isinstance(hast, dict):

                        hashtext = hast['text']

                        for letter in hashtext:
                            if letter not in string.ascii_letters:
                                hashtext = hashtext.replace(letter,"")
                        hashtext = str(hashtext).lower()
                        if len(hashtext)>0:
                            templist.append(hashtext)

                #pairs has been imported and added to global
                if len(templist)>0:
                    created_at = time.strptime(created_at[11:19] , "%H:%M:%S")

                    if(latest < created_at):
                        latest = created_at

                    if  latest.tm_min - created_at.tm_min < tinterval.tm_min  :
                        graph.add_node(hashtext)
                        pairs.append(templist)
                templist = []


        except KeyError:
            pass

    return pairs

def get_edges_from_pairs(pairs):

    pair_listed = []

    for line in pairs:

        if len(line)>2:
            for i in range( 1 , len(line)):
                for j in range(1 ,len(line)):
                    if i!=j:
                        pair_listed.append(tuple([line[i],line[j]]))

    return pair_listed

def calc_average_degree():
    global graph
    global file_dir

    node_degree = nx.degree(graph).items()
    len_nodes = len(node_degree)
    total_degree = 0
    for i in node_degree:
        total_degree += i[1]
    avr_degree =  total_degree / len_nodes
    with open(file_dir + 'tweet_output/ft2.txt', "w") as text_file:
        text_file.write('\n'+ str(avr_degree))
    text_file.close()

def tweet_flow():
    global graph

    print "Incoming Tweets!"
    hashtag_edges = []
    hastag_edges = get_edge_from_pairs(genereate_tags())
    graph = max(nx.connected_component_subgraphs(graph), key=len)
    for i in hastag_edges:
        if i[0] != i[1] and len(i[0]) > len(i[1]):
            graph.add_edge(i[0],i[1])

    calc_average_degree()


    nx.draw_spectral(graph,
    node_size = 300,   # node_size can either take a single value (where all nodes will be size N),
                             # or a list of values, where Nth list value will be the size for the Nth node
    width = 100,  # similarly, the Nth value corresponds to the width for edge N
    node_color = '#A0CBE2', #light blue
    edge_color = '#4169E1', #royal blue
    font_size = 10,
    with_labels = True )

    plt.show(block = False)

    time.sleep(15)
    graph.clear()
    plt.close()
    tweet_flow()





file_dir = os.path.dirname(os.path.realpath(__file__))
file_dir = file_dir[:-3]
file_dir = string.replace(file_dir,"\\","/")
tinterval = latest = time.strptime("00:01:00" , "%H:%M:%S")
latest = time.strptime("00:00:00" , "%H:%M:%S")
graph = nx.Graph()
tweet_flow()





