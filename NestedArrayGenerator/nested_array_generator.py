def inorderTraversal(arr):
    for item in arr:
        if isinstance(item, int):
            yield item
        elif isinstance(item, list):
            yield from inorderTraversal(item)