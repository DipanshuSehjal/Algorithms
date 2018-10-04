"""
What will I learn: 
In this puzzle, you will learn to store data in a graph data structure. Searching through and updating the graph you’ve created will help you get to grips with Graph Theory.

External resources Graph TheoryBreadth First Search 

The goal:
Your virus has caused a backdoor to open on the Skynet network enabling you to send new instructions in real time.

You decide to take action by stopping Skynet from communicating on its own internal network.

Skynet's network is divided into several smaller networks, in each sub-network is a Skynet agent tasked with transferring information by moving from node to node along links and accessing gateways leading to other sub-networks.

Your mission is to reprogram the virus so it will sever links in such a way that the Skynet Agent is unable to access another sub-network thus preventing information concerning the presence of our virus to reach Skynet's central hub.

https://www.codingame.com/ide/puzzle/skynet-revolution-episode-1

"""

import sys
import math
from collections import deque
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]


class Graph():
    ''' Graph class that stores the nodes and edges of an undirected graph.
     A graph data structure consists of a set of nodes together
     with a set of edges, which are unordered
     pairs of nodes indicating that two nodes are
     connected to one another.'''

    def __init__(self, edges=None):
        ''' The __init__ method accepts one optional
        argument called edges that is an
        iterable of 2-tuples containing the two nodes that are connected.
        It uses an adjacency list to store the nodes and edges
        Adjacency list is implemented with a dictionary'''
        
        self.adj={}
        if edges is not None:
            for edge in edges:
                self.add_edge(edge[0],edge[1])


    # iterable
    def __iter__(self):
        return iter(self.adj)  # it returns a dict which is iterable


    #indexing
    def __getitem__(self, item):
        return self.adj[item]


    #in
    def __contains__(self, item):
        return item in self.adj.keys()


    def bfs(self,s, ex, delete=True):
        '''The bfs method takes one argument,
        a starting node, and returns an iterable of 2-tuples
        of the form (node, distance) produced
        by performing a breadth-first search starting at the
        specified node.
        BFS is a traversing algorithm where you should start
        traversing from a selected
        node (source or starting node) and
        traverse the graph layerwise
        thus exploring the neighbour nodes (nodes which are directly connected to
        source node). You must then move towards the
        next-level neighbour nodes.
        As the name BFS suggests,
        BFS traverses the graph breadthwise as follows:
        1. First move horizontally and visit all the nodes of the current layer
        2. Move to the next layer
        Pseudo Code:
        BFS (G, s)                   //Where G is the graph and s is the source node
        Initialize all vertices with distance +inf and color = white
        color of s = gray ( mark s as visited )
        distance of s = 0
        Q.enqueue( s )
          while ( Q is not empty)
               //Removing that vertex from queue,whose neighbour will be visited now
               v  =  Q.dequeue( )
              //processing all the neighbours of v
              for all neighbours w of v in Graph G
                   if w is not visited
                            Q.enqueue( w ) //Stores w in Q to further visit its neighbour
                            mark w as visited(Black).'''

        if s in self.adj.keys():
            dist,color, par={},{},{}
            q=deque()
            for u in self.adj.keys():
                dist.update({u:math.inf})
                color.update({u:'White'})
                par.update({u:'NIL'}) #  intitialize
            dist[s]=0
            color[s]='Gray'
            par[s] = 'NIL'
            q.append(s)
            while len(q)!=0 :
                u=q.popleft()
                for v in self.adj[u]:
                    if color[v]=='White':
                        color[v]='Gray'  # assign new value
                        dist[v]=dist[u]+1
                        par[v] = u
                        q.append(v)
                color[u]='Black'
            # out=[]
            # for u in dist.keys():
            #     out.append((u,dist[u]))
            # return out
            
            # delete/pop the key
            if delete:
                c1 = par.pop(ex)
            # return par[ex], ex
                
                tmp = self.adj[c1]
                tmp.remove(ex)
                self.adj[c1] = tmp
                
                tmp = self.adj[ex]
                tmp.remove(c1)
                self.adj[ex] = tmp
                return c1, ex
            else:  # return distance
                return dist[ex]
                
        else:
            print(f'{s} not available in graph')


    def distance(self, u, v):
        '''The distance method takes two arguments that are nodes
        and returns the length of the shortest path between them.
        Note that when a node is reached
        in a breadth-first search, it has done so via a shortest path.
        u,v are source and end vertex for which we want to find
        shortest path. Call bfs(u) and find the shortest
        distance from u to v
        '''
    
        # original
        # for node, distance in self.bfs(u):
        #     if node==v:
        #         return distance
        
        
        
        return self.bfs(u, v, delete=False)
    
    def add_node(self, node):
        '''The add_node method accepts a single argument representing
        a node and adds it to the graph if it is not already present.'''
        if node not in self.adj.keys():
            self.adj.update({node:None})


    # instance methods
    def add_edge(self, u, v):
        '''The add_edge method accepts two arguments
        representing two nodes that are connected via
        an edge. The edge is added to the graph if
        it is not already present. Note that since this is an undirected graph,
        having an edge (u, v) in the graph implies that
        there is also an edge (v, u).'''

        if u in self.adj.keys():
            if self.adj[u]==None:
                self.adj.update({u: [v]})
            else:
                self.adj[u].append(v)
        else:
            self.adj.update({u:[v]})

        if v in self.adj.keys():
            if self.adj[v]==None:
                self.adj.update({u: [v]})
            else:
                self.adj[v].append(u)       # append values to a key, if earlier value is mutable & iterable
        else:
            self.adj.update({v:[u]})        # update adds a key and overwrites value




g = Graph()
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    g.add_edge(n1, n2) # make a link b/w the nodes in the dicti

    
ex_list = []
gr = []

for i in range(e):
    ei = int(input())  # the index of a gateway node
    ex_list.append(ei)

i=0
# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    
    dist = 1000
    if len(ex_list) == 1:
        c1, c2 = g.bfs(si, ei)
    # else:
    #     c1, c2 = g.bfs(si, ex_list[i])
    #     i += 1
    else: # this is if the exit nodes are more than 1
        for ex in ex_list:
            tmp = g.distance(si, ex)
            if tmp < dist:
                dist = tmp
                exit_node = ex
        c1, c2 = g.bfs(si, exit_node)
            
    # To debug: print("Debug messages...", file=sys.stderr)
    
    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(str(c1) + " " + str(c2))