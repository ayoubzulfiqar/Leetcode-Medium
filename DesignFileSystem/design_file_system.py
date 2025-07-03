class FileSystem:

    def __init__(self):
        self.root = {}

    def create(self, path: str, content: str) -> None:
        parts = path.split('/')
        current = self.root
        for i in range(1, len(parts)):
            part = parts[i]
            if i == len(parts) - 1:
                current[part] = content
            else:
                if part not in current:
                    current[part] = {}
                current = current[part]

    def mkdir(self, path: str) -> None:
        parts = path.split('/')
        current = self.root
        for i in range(1, len(parts)):
            part = parts[i]
            if part not in current:
                current[part] = {}
            current = current[part]

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = filePath.split('/')
        current = self.root
        for i in range(1, len(parts)):
            part = parts[i]
            if i == len(parts) - 1:
                if part in current and isinstance(current[part], str):
                    current[part] += content
                else:
                    current[part] = content
            else:
                if part not in current:
                    current[part] = {}
                current = current[part]

    def readContentFromFile(self, filePath: str) -> str:
        parts = filePath.split('/')
        current = self.root
        for i in range(1, len(parts)):
            part = parts[i]
            if i == len(parts) - 1:
                return current[part]
            else:
                current = current[part]
        return ""