"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1:
Partner 2:
Date:
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    ans = []
    ##### Your implementation goes here. #####
    if (alg == 'DFS'):
        st = Stack()
        maze.start.visited = True
        st.push(maze.start)
        while (st.isEmpty() != True):
            curr = st.pop()
            for neighbor in curr.neigh:
                if neighbor.visited != True:
                    neighbor.visited = True
                    st.push(neighbor)
                    neighbor.prev = curr
        trace = maze.exit
        while trace != None:
            ans.insert(0,trace.rank)
            trace = trace.prev
        #print(ans)
    ##### Your implementation goes here. #####
    if (alg == 'BFS'):
        distance = 0
        st = Queue()
        maze.start.visited = True
        maze.start.dist = distance
        st.push(maze.start)
        while (st.isEmpty() != True):
            distance += 1
            curr = st.pop()
            for neighbor in curr.neigh:
                if neighbor.visited != True:
                    neighbor.visited = True
                    neighbor.dist = distance
                    st.push(neighbor)
                    neighbor.prev = curr
        trace = maze.exit
        while trace != None:
            ans.insert(0, trace.rank)
            trace = trace.prev
        #print(ans)
    return ans
"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
