from union_find import UnionFind
from random import shuffle


def minSpanningTree(nodes, edges):
    '''
    Input:
    A set of nodes and a set of edges, where each edge is
    specified by a tuple (u,v) where u,v are distinct nodes
    in "nodes".

    Output:
    A set of edges that forms a minimum-weight spanning tree
    of the graph (if it is connected).

    Running time: O( |E|*log |E| )
    '''
    mst = []
    shuffle(edges) # randomizes the edges to be connected 

    uf = UnionFind(nodes)

    for e in edges:
        if uf.union(e[0], e[1]):
            mst.append((e[0], e[1], 1))  # each edge is given a weight 1

    return mst

def path_search(g, start):
    '''
    Finds the longest possible route through the maze from start with no detours or
    backtracking.

    Args: g is the undirected graph representing the paths in the maze, start is the
    point (x, y) that we begin searching from.

    Returns the route as a list with the first entry as the start and the last 
    entry as the end. 
    '''
    R = {}
    dist = {}
    S = []  # priority queue
    max_val = 0

    S.append(((start, start), 0))
    while len(S) > 0: # Dijkstra's algorithm
        popped = S.pop(0)
        prev, curr = popped[0][0], popped[0][1]
        val = popped[1]
        if curr not in R.keys():
            R[curr] = prev
            dist[curr] = val
            # add each outgoing edge (curr,succ) from curr to S
            for succ in g.neighbours(curr):
                if succ != prev:  # prevent "walk backwards"
                    S.append(((curr, succ), val+1))
                    if val + 1 > max_val:
                        max_key = succ

    path = [max_key]
    while path[-1] != start:
        for v in R.keys():
            if v == path[-1]:
                path.append(R[v])
                break
    path.reverse()
    return path