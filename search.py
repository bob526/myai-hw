# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).

  You do not need to change anything in this class, ever.
  """

  def getStartState(self):
     """
     Returns the start state for the search problem
     """
     util.raiseNotDefined()

  def isGoalState(self, state):
     """
       state: Search state

     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state

     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take

     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].

  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"

  
  myDFSAnswer = []    # List of actions
  nodeTraveled = []   # List of tuple(x,y)
  myDFSStack = util.Stack()
  # Declare the variable.

  myNextInfo = problem.getSuccessors(problem.getStartState())
  nodeTraveled += [problem.getStartState()]  # Remember to add []

  # First push to stack
  for x in range(len(myNextInfo)):

    myDFSStack.push((myNextInfo[x][0],[myNextInfo[x][1]]))
  while (not myDFSStack.isEmpty()):
    temp = myDFSStack.pop()
    dfsCurrentPoint = temp[0]
    dfsCurrentAction = temp[1]
    if problem.isGoalState(dfsCurrentPoint) is True:
      return dfsCurrentAction

    if ((dfsCurrentPoint) not in (nodeTraveled)):
      nodeTraveled += [dfsCurrentPoint]
      myNextInfo = problem.getSuccessors(dfsCurrentPoint)
      for x in range(len(myNextInfo)):
        myDFSStack.push((myNextInfo[x][0], dfsCurrentAction + [myNextInfo[x][1]]))

  return []
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  nodeTraveled = []   # List of tuple(x,y)
  myBFSQueue = util.Queue()
  
  myCurrentPoint = problem.getStartState()
  myBFSQueue.push((myCurrentPoint,[]))
  nodeTraveled += [myCurrentPoint]

  while not myBFSQueue.isEmpty():
    temp = myBFSQueue.pop()
    myCurrentPoint = temp[0]
    myCurrentAction = temp[1]
    if problem.isGoalState(myCurrentPoint) is True:
      return myCurrentAction
    myNextInfo = problem.getSuccessors(myCurrentPoint)
    for x in range(len(myNextInfo)):
      if myNextInfo[x][0] not in nodeTraveled:
        nodeTraveled += [myNextInfo[x][0]]
        myBFSQueue.push((myNextInfo[x][0], myCurrentAction+[myNextInfo[x][1]] )) 

  return []
  util.raiseNotDefined()

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  nodeTraveled = [] #A list of tuple
  myPriorityQ = util.PriorityQueue()
  
  myCurrentPoint = problem.getStartState()
  nodeTraveled += [myCurrentPoint]
  myRealCost = 0
  #myPriorityQ(((x,y)poistion, action"s",cost), priority(admissible cost))
  myPriorityQ.push((myCurrentPoint,[],myRealCost),  heuristic(myCurrentPoint,problem))
  while not myPriorityQ.isEmpty():
    temp = myPriorityQ.pop()
    myCurrentPoint = temp[0]
    myCurrentActions = temp[1]
    myRealCost = temp[2]
    if problem.isGoalState(myCurrentPoint) is True:
      return myCurrentActions
    nextStepInfo = problem.getSuccessors(myCurrentPoint)
    for x in range(len(nextStepInfo)):
      if nextStepInfo[x][0] not in nodeTraveled:
        nodeTraveled += [nextStepInfo[x][0]]
        estiCost = heuristic(nextStepInfo[x][0],problem)
        admissibleCost = myRealCost+estiCost
        myPriorityQ.push( (nextStepInfo[x][0],myCurrentActions+[nextStepInfo[x][1]],myRealCost+nextStepInfo[x][2]), admissibleCost)

  return []
  util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
