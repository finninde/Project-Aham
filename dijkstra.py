from heapq import heappush, heappop
import itertools

def flatten_list(input_list):
    while len(input_list) > 0:
        yield input_list[0]
        input_list = input_list[1]
    return input_list

## Implements dijkstras algorithm for finding the shortest path in a graph from a given start point
def dijkstra(undirectedgraph, sourcenode):
    S = []

    ##Implementation of min-priority queue from https://docs.python.org/2/library/heapq.html
    Q = []                         # list of entries arranged in a heap
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-task>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count

    def add_task(task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in entry_finder:
            remove_task(task)
        count = next(counter)
        entry = [priority, count, task]
        entry_finder[task] = entry
        heappush(Q, entry)

    def remove_task(task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop_task():
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while Q:
            priority, count, task = heappop(Q)
            if task is not REMOVED:
                del entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')
    ## CODE FROM https://docs.python.org/2/library/heapq.html END

    nodedata = {}
    for node in undirectedgraph.nodes:
        nodedata[node] = [float("inf"), None] # Distance from source + parent attributes
        add_task(node, float("inf"))          # We add all tasks with such a priority that it will be called last

    add_task(sourcenode, 0)         #Change priority of source node to 0. We wish to start with the source node.

    while len(Q)>1:            #While there are nodes in the min-priority queue
        ##PSEUDOCODE START
        u = pop_task() #extract-min(Q)              #Get the node with the lowest priority/distance
        S.append([u])                              #Get the intersection of the set of shortest path vertices and u (append u)

        if(undirectedgraph.edges.get(u)):
            for v in undirectedgraph.edges[u]:    ## Should be Key (endnode) which we use to get Edgedata (see class UndirectedGraph)
                # Relax each edge! Remember to update each priority in the minqueue by calling add_task(task, priority)
                # Do we need to remember parent? Seems like we only need to remember source (first element in S for this task?

                w = undirectedgraph[(u.latitude, u.longitude)][(v.latitude, v.longitude)].weight    # Get the weight of the line/road
                #u.d is found above
                v.d = entry_finder[v][0]    #Should give us the current distance from source. Inf = not connected

                if v.d > u.d + w:           #If the newfound distance from sourcenode is less than what is saved in the priorityqueue
                    add_task(v, (u.d+w))        #Update v in the priority queue with the new distance from source

                    # Remember that nodedata is a dict where each key leads to a tuple value: weight (distance from source) and parent
                    nodedata[v][0] = u.d + w    #Update the distance from source as well in nodedata
                    nodedata[v][1] = u          #Update the parent in the shortest path for the node in nodedata.
    
    return nodedata
