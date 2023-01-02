
def minimumDistance(dist, inc):
    val= sys.maxsize
    min_index=0
    l= len(dist)
   
    for i in range(0, l):
        if inc[l]== False and val>= dist[l]:
            val = dist[v]
            min_index=l
    return min_index


def printDis(dist):
    for i in range(0,len(dist)):
        print(dist[i])
   


def dijkstra(graph,src):
    l = len(graph)
   
    distance=[sys.maxsize]*l
   
    included=[False]*l
   
    distance[src]=0
   
    for count in range(0,l-1):
        minDistance=minimumDistance(distance, included)
       
        included[src]=0
       
        for i in range(0,l):
            if (!included[v] and graph[u][v] and distance[u] != sys.maxsize and distance[u] + graph[u][v] < distance[v]):
                distance[v] =  distance[u] + graph[u][v]
               
       
    printDis(distance)
   



   
   
   
   
   
   

if __name__='__main__':
    graph= [[0,30,10,20],
      [30,0,25,9999],
      [10,25,0,15],
      [20,0,15, 9999]]
   
    dijkstra(graph,0)
