"""Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B 
such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  
Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, 
and it doesn't contain any element twice.

https://leetcode.com/problems/is-graph-bipartite/description/

"""

class Solution:
    color = {}
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        """
        DFS
        :param graph: adj list
        :return: boolean
        """
        global color
        color = {}
        for i in range(len(graph)):
            color[i] = "white"


        for i in range(len(graph)):
            if color[i] == "white":
                color[i] = "red"        # start color
                if Solution.DFS_visit(graph, i) is False:
                    return False

        return True

    def DFS_visit(graph, u):
        for v in graph[u]:
            if color[v] == "white":

                color[v] = "blue" if color[u] == "red" else "red"
                if Solution.DFS_visit(graph, v) is False:
                    return False

            elif color[v] == color[u]:
                return False
