import attrs

@attrs.define
class FailedGetInstructionsError(Exception):
    """Raise When Failed to get Instructions
    """
    error_msg: str

@attrs.define
class FailedCalculateFeeError(Exception):
    """
    Raise When Failed Calculate Fee
    """
    error_msg: str

@attrs.define
class FailedListingTransactionsError(Exception):
    """
    Raise when failed listing transactions
    """
    error_msg: str

@attrs.define
class FailedCreateTransactionsError(Exception):
    """
    raise when failed create transaction
    """
    error_msg: str

@attrs.define
class FailedGetDetailTransaction(Exception):
    """
    raise when failed to get detailed closed transaction
    """
    error_msg: str