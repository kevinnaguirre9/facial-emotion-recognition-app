
class ClassNotFound( Exception ):
    def __init__ (self, message : str|None = None ):
        super().__init__ (message or 'Class not found')