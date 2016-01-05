
class GmxException(RuntimeError):
    """There was an ambiguous exception that occurred while handling your
    request."""

class ConnectionError(GmxException):
    """A Connection error occurred."""

class AuthenticationError(GmxException):
    """GMX Authentication failed."""

class Timeout(GmxException):
    """The request timed out."""
