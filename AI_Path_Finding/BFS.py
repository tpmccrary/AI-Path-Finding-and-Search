import queue

class BFS:
    
    def BFS(map, start, goal):
        queue = [[start, []]] # starting point, empty path
        queue.append(s)

        #1-5 are allowed paths
        #0s are not allowed paths

        if start == goal:
           return

        while len(queue)>0:
            node, path = queue.pop()
            path.append(node)
            visited(node, v)

            if node == end:
                return path

            adj_nodes = neighbors(node, map)
            
            for item in adj_nodes:
                if not visited(item, v):
                    queue.append((item, path[:]))
        
        return None