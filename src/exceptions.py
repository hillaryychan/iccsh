class IccshValueError(Exception):
    def __init__(self, message="Command called with invalid values"):
        self.message = message
        super().__init__(self.message)
