"""N-ary tree data structure for hierarchical location organization"""


class NaryTreeNode:
    """
    N-ary tree node for implementing hierarchical location structure.
    Useful for organizing locations by regions, countries, cities, etc.
    """

    def __init__(self, data):
        """
        Initialize an N-ary tree node.

        Args:
            data: The data to store in the node (e.g., location name)
        """
        self.data = data
        self.children = []

    def add_child(self, child_node):
        """
        Add a child node to this node.

        Args:
            child_node (NaryTreeNode): The child node to add
        """
        self.children.append(child_node)

    def find(self, data):
        """
        Find a node with the given data using depth-first search.

        Args:
            data: The data to search for

        Returns:
            NaryTreeNode: The node if found, None otherwise
        """
        if self.data == data:
            return self
        for child in self.children:
            found = child.find(data)
            if found:
                return found
        return None

    def __repr__(self):
        return f"NaryTreeNode({self.data})"
