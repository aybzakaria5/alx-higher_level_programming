#!/usr/bin/python
""" a locked clss that prevents the usuer
    from dynamically creating an instance
"""


class LockedClass:
    """preventing the user from creating an
    instance
    """
    __slots__ = ['first_name']
