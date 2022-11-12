import csv
edgeFile = 'edges.csv'
from queue import Queue 

def bfs(start, end):
    # Begin your code (Part 1)
    """------------------Explanation-------------------
    For bfs, I use a FIFO queue to store the nodes which may be visited later. 
    First of all, open the edges.csv file and read by csv.reader function as “lines”, 
    and the variable “line” means each row within the csv file, which contains every 
    column of the row.Then if the first column is “start” represents that it’s the 
    first row, containing the column information. The dictionary “dict” stores every 
    tuples’ ( roads’ begin and end point ) distances and speed limits. The dictionary 
    “next” stores the nodes that can be reach by each start points. And the dictionary 
    “visited” tells if a node is visited by the searching algorithm, set them as 0 first.
    The residual steps involve the searching algorithm. Set the number of node visited, 
    and accumulative distance as 0, put the start point into the queue, and the previous 
    point of start point is itself, and the start point is visited. Then keep the 
    while-loop running until queue is empty or the end point is discovered, each time 
    pick a element from the queue, and use the dictionary to find its neighbor nodes, 
    if they are not yet be visited, put them into  the queue, and set their previous 
    node as the current node pulling out from the queue.
    Since it is required to return a list which contains the found path’s nodes within 
    the order, so I start from the end point, and use the dictionary “prev” to get its 
    parent node, and with the while-loop the roads are pushing into the path sequentially. 
    
    """
    q = Queue()
    dict = {}
    next = {}
    visited = {}
    prev = {}
    with open(edgeFile,newline = '') as file:
      lines = csv.reader(file)
      for line in lines:
        if(line[0] == "start"): continue
        dict[ (int(line[0]),int(line[1])) ] = (float(line[2]),float(line[3]))
        if(int(line[0]) not in next):
          next[int(line[0])] = []
        next[int(line[0])].append(int(line[1]))
        visited[int(line[0])] = 0
        visited[int(line[1])] = 0
    num = 0
    path = []
    dist = 0
    q.put(start)
    path.append(start)
    prev[start] = start
    visited[start] = 1
    while not q.empty():
      now = q.get()
      num += 1
      if(now not in next): continue
      for neighbor in next[now]:
        if(visited[neighbor] == 0):
          visited[neighbor] = 1
          prev[neighbor] = now
          q.put(neighbor)
          if(neighbor == end):
            while not q.empty(): q.get()
            break
    r = end
    l = prev[end]
    # start != end
    while 1:
      path.insert(1, r)
      dist += dict[ (l,r) ][0]
      r = l
      if( l == prev[l] ): break
      l = prev[l]
    
    return path, dist, num
    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
