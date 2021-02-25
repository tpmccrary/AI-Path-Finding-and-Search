# AI-Path-Finding-and-Search

***

This asssignment focuses on simplified pathfinding problems using Breath First Search (BFS) with a 3 minutes time cuttoff. The problem will search for the shortest path from a given start location to a given goal location on a square grid which is weighted. The agent is allowed to move in directions: up, down, left & right; however, they are not allowed to move diagonally or outside the bounds of the map. The algorithm implements repeat-state checking, thus we do not revisit states that have already been visited.  
##### The code prints out the following information:

                1.	The cost of the path found
                2.	The number of nodes expanded 
                3.	The maximum number of nodes held in memory
                4.	The runtime of the algorithm in milliseconds
                5.	The path as a sequence of coordinates 

The algorithm prints 1 for path cost and Null for path sequence if it terminates without finding a result.

## Table of Contents

                1) ai_path_finding.py 
                2) AI_Path_Finding.py (Folder)
                        a) BFS.py
                        b) algorithm_stats.py
                        c) map_grid.py
                3) test (Folder)
                        a) map.txt
                        b) map2.txt
                        c) map3.txt
                4) README.md

## Technologies used 

1. Python: Version 3.9.2
2. Visual Studio Code: Version 1.53.2
3. Git Hub: Version 2.6.3

## Instillation 
git clone https://github.com/tpmccrary/AI-Path-Finding-and-Search.git

## How to Run the Code
1. command to run test 1: python3 ai_path_finding.py test/map.txt BFS
2. command to run test 2: python3 ai_path_finding.py test/map.txt2 BFS
3. command to run test 3: python3 ai_path_finding.py test/map.txt3 BFS