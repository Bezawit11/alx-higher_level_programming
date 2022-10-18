#!/usr/bin/python3
class LockedClass:
    """A locked class that lets the user dynamically create the instance
    attribute 'first_name' only"""
    __slots__ = ['first_name']
