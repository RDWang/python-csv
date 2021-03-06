#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/07/23 17:54:18 $
#   $RCSfile: depthFirstBranchAndBoundSolver.py,v $
#   $Revision: 1.3 $
#
#   $Id: depthFirstBranchAndBoundSolver.py,v 1.3 2003/07/23 17:54:18 brpreiss Exp $
#

"""
Provides the DepthFirstBranchAndBoundSolver class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/07/23 17:54:18 $"
__version__ = "$Revision: 1.3 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.solver import Solver

#{
class DepthFirstBranchAndBoundSolver(Solver):
    """
    Depth-first brand-and-bound solver.
    """

    def __init__(self):
        """
        (DepthFirstBranchAndBoundSolver) -> None
        Constructor.
        """
        super(DepthFirstBranchAndBoundSolver, self).__init__()

    def search(self, current):
        """
        (DepthFirstBranchAndBoundSolver, Solution) -> Solution
        Does a depth-first traversal of the solution space
        starting from the given node.
        """
        if current.isComplete:
            self.updateBest(current)
        else:
            for successor in current.successors:
                if successor.isFeasible and \
                        successor.bound < self._bestObjective:
                    self.search(successor)
#}>a
