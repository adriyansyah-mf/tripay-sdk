import attrs

@attrs.define
class FailedGetInstructionsError(Exception):
    """Raise When Failed to get Instructions
    """
    error_msg: str
    