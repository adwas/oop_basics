import sys, types, pprint

class Vector:
    """
    Demo of a class with multiple signatures for the constructor
    """
    def __init__(self, *args, **kwargs):
        
        if len(args) == 1:  foundOneArg = True;  theOnlyArg = args[0]
        else:               foundOneArg = False; theOnlyArg  = None

        if foundOneArg and isinstance(theOnlyArg, list):      
            self.initializeFromList(theOnlyArg)             
        elif foundOneArg and isinstance(theOnlyArg,Vector):
            self.initializeFromVector(theOnlyArg)           
        else:
            self.initializeFromArgs(*args)

        pprint.pprint(self.values)  # for debugging only
        
    def initializeFromList(self, argList):
        self.values = [x for x in argList]

    def initializeFromVector(self, vector):
        self.values = [x for x in vector.values]

    def initializeFromArgs(self, *args):
        self.values = [x for x in args]
#------------ end of class definition ---------------------

v = Vector(1,2,3) 
v = Vector([4,5,6]) 
q = Vector(v)


# but there is much more better advenced way 
# see https://gist.github.com/anonymous/335850