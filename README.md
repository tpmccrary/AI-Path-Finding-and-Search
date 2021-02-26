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
        |   |-- map_grid.py
        |
        |-- test/
        |   |-- map.txt
        |   |-- map2.txt
        |   |-- map3.txt
        |    
        |-- ai_path_finding.py
        |-- README.md

## How to Run the Code
In order to run the code, you must be in the root directory and use these commands:

1. Command to run test 1: **python3 ai_path_finding.py test/map.txt BFS**
2. Command to run test 2: **python3 ai_path_finding.py test/map2.txt BFS**
3. Command to run test 3: **python3 ai_path_finding.py test/map3.txt BFS**

## Technologies used 

1. Python: Version 3.9.2
2. Visual Studio Code: Version 1.53.2
3. Git Hub: Version 2.6.3




