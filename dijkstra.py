from heapq import heappush, heappop
import itertools

# Finds shortest path between a source and a target
def dijkstra(undirectedgraph, sourcenode, targetnode):
    # Contains the Dijkstra algorithm output
    nodedata = {}

    # Implementation of min-priority queue from https://docs.python.org/2/library/heapq.html
    Q = []                          # list of entries arranged in a heap
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-task>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count

    def add_task(task, priority=0):
        # Add a new task or update the priority of an existing task
        if task in entry_finder:
            remove_task(task)
        count = next(counter)
        entry = [priority, count, task]
        entry_finder[task] = entry
        heappush(Q, entry)

    def remove_task(task):
        # Mark an existing task as REMOVED.  Raise KeyError if not found.
        entry = entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop_task():
        # Remove and return the lowest priority task. Raise KeyError if empty.
        while Q:
            priority, count, task = heappop(Q)
            if task is not REMOVED:
                del entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')
    # CODE FROM https://docs.python.org/2/library/heapq.html END

    for node in undirectedgraph.nodes:
        nodedata[node] = [float("inf"), None] # Distance from source + parent attributes
        add_task(node, float("inf"))          # All nodes are set with priority infinite
    add_task(sourcenode, 0.0)
    nodedata[sourcenode] = [0, None]

    while len(Q)>1:
        u = pop_task()
        if u == (targetnode):    #If we have arrived at the end-node, dijkstra
            break

        if(undirectedgraph.edges.get(u)):
            for v in undirectedgraph.edges[u]:
                w = undirectedgraph[u][v].weight    # Get the weight of the line/road
                u.d = nodedata[u][0]
                v.d = entry_finder[v][0]    #Should give us the current distance from source. Inf = not connected

                if v.d > u.d + w:
                    add_task(v, (u.d+w))        #Update v in the priority queue

                    nodedata[v][0] = u.d + w    #Update v's weight
                    nodedata[v][1] = u          #Update v's parent

    # Now we should have a Dijkstra tree. Crawl from target to source by utilizing the parent attribute.
    # When crawling, add each node to a result stack that shall return the shortest path between
    # target and source. Also include a return with the total distance from target to source

    shortestDistance = nodedata[targetnode][0]
    resultStack = []

    resultStack.append(targetnode)

    while nodedata[resultStack[-1]][1] is not None:  #while we arent at the sourcenode... (only one that shouldnt have parent)
        resultStack.append(nodedata[nodedata[resultStack[-1]][1]])  #add the parent!

    #Return stack with path of nodes sourcenode -> targetnode, float distance to targetnode from source
    return resultStack, shortestDistance
