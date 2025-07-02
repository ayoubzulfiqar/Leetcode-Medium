def classify_tree_nodes(tree_data: list[dict]) -> list[dict]:
    """
    Classifies each node in a tree as 'Root', 'Inner', or 'Leaf'.

    Args:
        tree_data: A list of dictionaries, where each dictionary represents a node
                   with 'id' and 'p_id' (parent id). p_id can be None for the root.

    Returns:
        A list of dictionaries, each containing 'id' and its determined 'type'.
    """
    
    # Collect all node IDs that appear as parent IDs, meaning they have children.
    nodes_that_are_parents = set()
    all_node_ids = set()

    for row in tree_data:
        all_node_ids.add(row['id'])
        if row['p_id'] is not None:
            nodes_that_are_parents.add(row['p_id'])

    result = []
    for node in tree_data:
        node_id = node['id']
        node_p_id = node['p_id']

        node_type = ""
        if node_p_id is None:
            # A node with a null parent ID is always the Root.
            node_type = "Root"
        elif node_id in nodes_that_are_parents:
            # A node with a parent (not root) and also has children is an Inner node.
            node_type = "Inner"
        else:
            # A node with a parent (not root) and no children is a Leaf node.
            node_type = "Leaf"
        
        result.append({'id': node_id, 'type': node_type})
    
    return result