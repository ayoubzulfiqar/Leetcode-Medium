def checkIfInstanceOf(obj, classFunction):
    if not isinstance(classFunction, type):
        return False
    return isinstance(obj, classFunction)