import queue

class BFS:
    
    def BFS(map, start, goal):
        visited = []
        queue = [[start]]
        
        if start == goal:
           return

        while queue:
            path = queue.pop()
            node = path[-1]

            if node is not visited:
                neighbors = map[node]

                for neighbors in neighbors:
                    new_path = list (path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                    if neighbor == goal:
                        print("shortest path = ", *new_path)
                        return 
                visited(append)