# AI-Path-Finding-and-Search
Authors of this project:
- Tashi Choden
- Timothy P. McCrary
***

## Team Member Contribution 
Both members (Tashi, Timothy) worked together when developing the code. This includes design, coding, testing, and documentation. 

## About
This asssignment focuses on simplified pathfinding problems using Breath First Search (BFS) with a 3 minutes time cuttoff. The problem will search for the shortest path from a given start location to a given goal location on a square grid which is weighted. The agent is allowed to move in directions: up, down, left & right; however, they are not allowed to move diagonally or outside the bounds of the map. The algorithm implements repeat-state checking, thus we do not revisit states that have already been visited.  
##### The code prints out the following information:

                1.	The cost of the path found.
                2.	The number of nodes expanded. 
                3.	The maximum number of nodes held in memory.
                4.	The runtime of the algorithm in milliseconds.
                5.	The path as a sequence of coordinates. 

The algorithm prints 1 for path cost and Null for path sequence if it terminates without finding a result.

## Project File Structure
        AI-Path-Finding-and-Search/
        |-- AI_Path_Finding/
        |   |-- __init__.py
        |   |-- algorithm_stats.py
        |   |-- BFS.py
        |   |-- ids.py
        |   |-- map_grid.py
        |
        |-- test/
        |   |-- map.txt
        |   |-- map2.txt
        |   |-- map3.txt
        |   |-- map4.txt
        |    
        |-- ai_path_finding.py
        |-- README.md

## How to Run the Code
In order to run the code, you must be in the root directory and use these commands:
### BFS
1. Test 1: **python3 ai_path_finding.py test/map.txt BFS**
2. Test 2: **python3 ai_path_finding.py test/map2.txt BFS**
3. Test 3: **python3 ai_path_finding.py test/map3.txt BFS**
4. Test 4: **python3 ai_path_finding.py test/map4.txt BFS**

### IDS
1. Test 1: **python3 ai_path_finding.py test/map.txt IDS**
2. Test 2: **python3 ai_path_finding.py test/map2.txt IDS**
3. Test 3: **python3 ai_path_finding.py test/map3.txt IDS**
4. Test 4: **python3 ai_path_finding.py test/map4.txt IDS**

## Performance on Test Cases

### BFS
1. Test 1 (5x5):
    - Cost of path: 14
    - Number of nodes expanded: 25
    - Max nodes in memory: 7
    - Runtime: 0.22280006669461727ms
    - Path to goal: [[1, 2], [2, 2], [3, 2], [4, 2], [4, 3]]
2. Test 2 (10x10):
    - Cost of path: 15
    - Number of nodes expanded: 39
    - Max nodes in memory: 10
    - Runtime: 0.35629999911179766ms
    - Path to goal: [[1, 2], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6]]
3. Test 3 (20x20):
    - Cost of path: 96
    - Number of nodes expanded: 363
    - Max nodes in memory: 20
    - Runtime: 6.577300024218857ms
    - Path to goal: [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2], [11, 2], [12, 2], [13, 2], [14, 2], [15, 2], [16, 2], [17, 2], [18, 2], [19, 2], [19, 3], [19, 4], [19, 5], [19, 6], [19, 7], [19, 8], [19, 9], [19, 10], [19, 11], [19, 12], [19, 13], [19, 14], [19, 15], [19, 16], [19, 17], [19, 18], [19, 19]]
4. Test 4 (10x10, inaccessible goal):
    - Cost of path: -1
    - Number of nodes expanded: 84
    - Max nodes in memory: 10
    - Runtime: 0.8950000010372605ms
    - Path to goal: NULL

### IDS
1. Test 1 (5x5):
    - Cost of path: 14
    - Number of nodes expanded: 23
    - Max nodes in memory: 22
    - Runtime: 0.20629999926313758ms
    - Path to goal: [[1, 2], [2, 2], [3, 2], [3, 3], [4, 3]]
2. Test 2 (10x10):
    - Cost of path: 15
    - Number of nodes expanded: 13
    - Max nodes in memory: 12
    - Runtime: 0.2669000023161061ms
    - Path to goal: [[1, 2], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6]]
3. Test 3 (20x20):
    - Cost of path: 215
    - Number of nodes expanded: 209
    - Max nodes in memory: 208
    - Runtime: 77.03010000113863ms
    - Path to goal: [[1, 2], [1, 1], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14], [0, 15], [0, 16], [0, 17], [0, 18], [0, 19], [1, 19], [1, 18], [2, 18], [2, 17], [3, 17], [3, 16], [3, 15], [3, 14], [4, 14], [4, 13], [4, 12], [4, 11], [4, 10], [4, 9], [4, 8], [4, 7], [4, 6], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14], [5, 15], [6, 15], [6, 16], [6, 17], [6, 18], [6, 19], [7, 19], [7, 18], [7, 17], [8, 17], [8, 18], [8, 19], [9, 19], [10, 19], [10, 18], [10, 17], [11, 17], [11, 16], [12, 16], [12, 17], [12, 18], [12, 19], [13, 19], [13, 18], [14, 18], [14, 19], [15, 19], [16, 19], [17, 19], [18, 19], [19, 19]]
4. Test 4 (10x10, inaccessible goal):
    - Cost of path: -1
    - Number of nodes expanded: 84
    - Max nodes in memory: 83
    - Runtime: 21.330999999918276ms
    - Path to goal: NULL

## Technologies used 

1. Python: Version 3.9.2
2. Visual Studio Code: Version 1.53.2
3. Git Hub: Version 2.6.3




