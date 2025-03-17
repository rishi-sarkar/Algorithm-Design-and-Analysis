#!/usr/bin/env python3
"""
ECE 406:  File for Exercise 2 of Assignment #4
"""

import numpy as np

################################################################################
# SUBMISSION INSTRUCTIONS FOR A4Q1
#   1. Write your username and student number in the box below
#   2. Submit your code as A4Q1-<WatIAMusername>.py to the LEARN Dropbox
#      where <WatIAMusername> is replaced by your WatIAM username
#   3. Submit a screencap of your bellman_ford function 
#      and the comment box containing your username and student
#      number to Crowdmark.
################################################################################

################################################################################
# student info
#
# WatIAM username: r6sarkar
# Student number: 20894095
################################################################################

def random_adjacency_matrix(n):
    """Produce a random n-by-n adjacency matrix for a directed graph with no self-loops

    NOTE: edge weights are integers that can be positive or negative
    NOTE: to make things simple, if (u, v) is an edge in the graph, then (v, u) is not
    """
    LAMBDA = 0.7 # parameter for the Poisson distribution
                 # higher LAMBDA means a more densely connected graph
                 # ...and densely connected graphs have more negative cycles...
    edge_magnitudes = np.random.poisson(lam=LAMBDA, size=(n, n))
    edge_directions = (-1) ** np.random.binomial(1, 0.5, size=(n, n))
    A = edge_magnitudes * edge_directions
    # finally, make some small adjustments to the graph
    for u in range(n):
        for v in range(n):
            if u == v:
                A[u, v] = 0 # no self loops allowed
            if A[u, v] and A[v, u]: # both edges currently exist; trim one
                if np.random.binomial(n=1, p=0.5): # simulate a coin flip
                    A[u, v] = 0
                else:
                    A[v, u] = 0
    return A



def plot_adjacency_matrix(A):
    """Turn an adjacency matrix representation of a graph into a plot of the graph
    
    ...then save the plot to a file on disk (by default `./graph.png`)
    """
    # NOTE: This function relies on extra python packages. Using it is entirely optional,
    #       although you might find it helpful for debugging
    import matplotlib
    matplotlib.use('Agg') # feel free to use your own preferred backend, or comment this
                          # out for interactive plotting (this hasn't been tested)
    import matplotlib.pyplot as plt
    import networkx as nx
    FILENAME = './graph.png' # change as needed
    G = nx.from_numpy_array(A, create_using=nx.DiGraph)
    nx.draw_shell(G, with_labels=True, arrows=True)
    labels = nx.get_edge_attributes(G,'weight')
    pos = nx.shell_layout(G)
    nx.draw_networkx_edge_labels(G,pos)
    plt.savefig(FILENAME)
    return


class Vertex():
    def __init__(self, index):
        self.index = index # index in the adjacency matrix that this vertex corresponds to
        self.dist = np.inf # current dist estimate in the B-F algorithm
        self.prev = None # current prev pointer; should be None or a Vertex


def bellman_ford(A, s):
    """Run Bellman-Ford on a graph with adjacency matrix A and start vertex s.

    Input: np.ndarray A representing the graph adjacency matrix, and integer s
           representing the starting vertex.
    Ouput: list of Vertex with proper dist and prev values corresponding to the 
           shortest paths found by the Bellman-Ford algorithm

    NOTE: we index starting at 0 in numpy so if A is n-by-n, then s should
          be an integer between 0 and n - 1 (inclusive)
    """

    def update(vertex_u, vertex_v, matrix_A):
        """Helper function for B-F: update the dist estimates along a single edges.

        Input: Vertex u and Vertex v representing the two ends of the edge, and
               np.ndarray A representing the graph adjacency matrix
        Ouput: None
               the function updates the prev and dist attributes of v as appropriate,
               but does not return anything
        """
        assert np.abs(A[vertex_u.index, vertex_v.index]) > 0, '(u, v) must be a valid edge (non-zero length) in A'
        if vertex_u.dist + matrix_A[vertex_u.index, vertex_v.index] < vertex_v.dist:
            vertex_v.dist = vertex_u.dist + matrix_A[vertex_u.index, vertex_v.index]
            vertex_v.prev = vertex_u
        return

    n, m = A.shape
    assert n == m, 'Only square matrices allowed'
    vertices = [Vertex(i) for i in range(n)]
    vertices[s].dist = 0
    
    for i in range(n - 1):
        for u in vertices:
            for v in vertices:
                if A[u.index, v.index] != 0:
                    update(u, v, A)

    for u in vertices:
        for v in vertices:
            if A[u.index, v.index] != 0 and u.dist + A[u.index, v.index] < v.dist:
                raise ValueError('Negative cycle detected')
                
    return vertices


def main():
    """
    Exercise 2: Implement Bellman-Ford
    """
    np.random.seed(4000000006) # comment this out for a truly random graph, which may be helpful for debugging
    #
    n = 4
    A = random_adjacency_matrix(n)
    print('The graph has the following adjacency matrix:')
    print(A)
    # plot_adjacency_matrix(A) # optional: comment this out if you want to save a plot of the graph to disk
    #
    s = 0 # index of the start vertex
    vertices = bellman_ford(A, s)
    print('final dists')
    print([v.dist for v in vertices])
    for z in range(n):
        if z != s:
            shortest_path = [vertices[z]]
            x = z # build the shortest path in backwards order, starting at destination vertex z
            if shortest_path[0].prev is None:
                print(f'No shortest path from {s} to {z} found')
                continue
            prev_vertex_index = vertices[shortest_path[0].prev.index].index
            while(prev_vertex_index != s and prev_vertex_index is not None): # check prev pointer for first vertex in current path
                # add prev vertex to begginning of current path
                shortest_path = [vertices[prev_vertex_index]] + shortest_path
                prev_vertex_index = vertices[shortest_path[0].prev.index].index
            # finally, start with the start vertex
            shortest_path = [vertices[s]] + shortest_path
            if len(shortest_path) == 1:
                print('No shortest path found')
            else:
                print(f'Shortest path from {s} to {z} is:')
                print([v.index for v in shortest_path])


if __name__ == '__main__':
    main()
