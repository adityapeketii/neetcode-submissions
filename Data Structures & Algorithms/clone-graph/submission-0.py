"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        start = node
        old_to_new = {}
        seen = set()
        seen.add(start)
        stack = []
        stack.append(start)

        while stack:
            node = stack.pop()
            old_to_new[node] = Node(val = node.val)
            for nei in node.neighbors:
                if nei not in seen:
                    stack.append(nei)
                    seen.add(nei)

        for old, new in old_to_new.items():
            for old_nei in old.neighbors:
                new_nei = old_to_new[old_nei]
                new.neighbors.append(new_nei)

        return old_to_new[start]


        