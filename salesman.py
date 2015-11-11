from dijkstra import dijkstra

## Implements a solution to the travelling salesman problem
def salesman(undirectedgraph):
    n = len(undirectedgraph.nodes)
    shortestPaths = [[float("inf")]*n]*n        # Produce an n*n matrix to store shortest paths between i-node and j-node

    #Lemma 24.17: Predecessor subgraph property: "The predecessor subgraph is a shortest-path tree rooted at s" (Cormen)

    for node in undirectedgraph.nodes:              ## For every node in the graph
        nodedata = dijkstra(undirectedgraph, node)  ## Call dijkstra with the given node as source node. A dict with all nodes and properties
        #nodedata now contains the shortest distances from source node to every other node
        #Is it necessary to call dijkstra more than once (are there several dijkstra shortest-paths?

        ## TODO: Go through the shortestPath-matrix, iterate through nodedata, **find nodes where the source node is parent** and see if distance is smaller
        for nodenumber in range(len(undirectedgraph.nodes)):
            nodeobject = undirectedgraph.nodes[nodenumber]
            nodeobjectproperties = nodedata[nodeobject]

            i = nodenumber

            for j in range(n):
                if(i==j):
                    shortestPaths[i][j] = 0

                if(shortestPaths[i][j] > nodeobjectproperties[0] and nodeobjectproperties[1] == node):
                    shortestPaths[i][j] = nodeobjectproperties[0]



            print(datanode)


        ## TODO: Use methods in optimizer to find solution to travelling salesman. One must ignore infinities.

    print (shortestPaths)