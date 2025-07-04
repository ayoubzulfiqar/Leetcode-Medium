from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def findRoot(self, nodes: List[Node]) -> Node:
        child_nodes_set = set()

        for node in nodes:
            for child in node.children:
                child_nodes_set.add(child)

        for node in nodes:
            if node not in child_nodes_set:
                return node
        
        return None