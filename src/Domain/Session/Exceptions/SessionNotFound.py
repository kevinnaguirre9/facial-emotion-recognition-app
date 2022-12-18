
class SessionNotFound ( Exception ):
    def __init__ (self, message : str|None = None ):
        super().__init__ (message or 'Session not found')