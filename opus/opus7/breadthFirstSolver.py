#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/07/23 17:54:18 $
#   $RCSfile: breadthFirstSolver.py,v $
#   $Revision: 1.3 $
#
#   $Id: breadthFirstSolver.py,v 1.3 2003/07/23 17:54:18 brpreiss Exp $
#

"""
Provides the BreadthFirstSolver class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/07/23 17:54:18 $"
__version__ = "$Revision: 1.3 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.solver import Solver
from opus7.queueAsLinkedList import QueueAsLinkedList

#{
class BreadthFirstSolver(Solver):
    """
    Breadth-first solver.
    """

    def __init__(self):
        """
        (BreadthFirstSolver) -> None
        Constructor.
        """
        super(BreadthFirstSolver, self).__init__()

    def search(self, initial):
        """
        (BreadthFirstSolver, Solution) -> Solution
        Does a breadth-first traversal of the solution space
        starting from the given node.
        """
        queue = QueueAsLinkedList()
        queue.enqueue(initial)
        while not queue.isEmpty:
            current = queue.dequeue()
            if current.isComplete:
                self.updateBest(current)
            else:
                for soln in current.successors:
                    queue.enqueue(soln)
#}>a
