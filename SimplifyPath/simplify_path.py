class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')

        for comp in components:
            if comp == "" or comp == ".":
                # Ignore empty strings (from multiple slashes) and current directory '.'
                continue
            elif comp == "..":
                # Go up one directory, if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory or file name
                stack.append(comp)

        # Construct the simplified path
        if not stack:
            return "/"
        else:
            return "/" + "/".join(stack)