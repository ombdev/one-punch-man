

class SignerError(Exception):
    """Exception when signing cfdi went bad"""
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return self.message
