class Dir:
    def __init__(self):
        self.contains = {}

class File:
    def __init__(self):
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = Dir()

    def ls(self, path: str) -> List[str]:
        paths = path.split("/")
        curDir = self.root
        for p in paths:
            if p == "":
                continue
            curDir = curDir.contains[p]
        if isinstance(curDir, Dir):
            return sorted(list(curDir.contains.keys()))
        else:
            return [paths[-1]]


    def mkdir(self, path: str) -> None:
        paths = path.split("/")
        curDir = self.root 
        for p in paths:
            if p == "":
                continue
            if not p in curDir.contains:
                curDir.contains[p] = Dir()
            curDir = curDir.contains[p]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        paths = filePath.split("/")
        curDir = self.root
        n = len(paths)
        for idx, p in enumerate(paths):
            if p == "":
                continue
            if not p in curDir.contains and idx != n - 1: # create Dir
                 curDir.contains[p] = Dir()
            elif not p in curDir.contains and idx == n - 1: # create file
                curDir.contains[p] = File()
            curDir = curDir.contains[p]
        curDir.content += content


    def readContentFromFile(self, filePath: str) -> str:
        paths = filePath.split("/")
        curDir = self.root
        for p in paths:
            if p == "":
                continue
            curDir = curDir.contains[p]
        
        return curDir.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)