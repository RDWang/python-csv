#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: orderedList.py,v $
#   $Revision: 1.16 $
#
#   $Id: orderedList.py,v 1.16 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the OrderedList class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.16 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.searchableContainer import SearchableContainer

#{
class OrderedList(SearchableContainer):
    """
    Base class from which all ordered list classes are derived.
    """

    def __init__(self):
        """
        (OrderedList) -> None
        Constructor.
        """
        super(OrderedList, self).__init__()

    def __getitem__(self, i):
        pass
    __getitem__ = abstractmethod(__getitem__)

    def findPosition(self, obj):
        pass
    findPosition = abstractmethod(findPosition)
#}>a

    def test(list):
        "OrderedList test program."
        print OrderedList.test.__doc__
        list.insert(1)
        list.insert(2)
        list.insert(3)
        list.insert(4)
        print list
        obj = list.find(2)
        list.withdraw(obj)
        print list
        position = list.findPosition(3)
        position.insertAfter(5)
        print list
        position.insertBefore(6)
        print list
        position.withdraw()
        print list
        for i in list:
            print i
    test = staticmethod(test)
