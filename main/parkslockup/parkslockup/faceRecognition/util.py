def getFileNameFromPath(path):
    withoutExten = path.split(".")[1]
    return withoutExten.split('/')[-1]