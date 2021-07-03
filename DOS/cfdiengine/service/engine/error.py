import enum
import sys
from misc.fmt import UMT


class FatalError(Exception):
    """ Fatal error exception class. """

    def __init__(self, msg=None):

        highlight = ''
        normal    = ''

        if sys.stderr.isatty():
            highlight = UMT.RED + UMT.BOLD
            normal    = UMT.NORMAL

        self.message = '%sFATAL%s: %s\n' % (highlight, normal, msg)

    def __str__(self):
        return self.message


class ErrorCode(enum.Enum):
    """
    Contains error codes that shall be
    communicated to consumer part of engine
    """
    SUCCESS = 0
    # values from 1 up to 200 are reserved
    # for answers of business handlers
    RESOURCE_NOT_FOUND = 192  # An element searched into resources is not there
    REQUEST_INVALID = 193     # It is not possible to consume request as it is comformed
    ETL_ISSUES = 197          # ETL means extract, transform, and load
    REQUEST_INCOMPLETE = 198  # Denotes a missing value in the request body expected
    DOCMAKER_ERROR = 199      # Problems related to docmaker stuff
    THIRD_PARTY_ISSUES = 200  # Lack interacting with third party entities

    # values from 201 up to 255 are reserved
    # for answers of engine mechanism
    MOTIVE_NOT_MANEUVERED = 201
    MOTIVE_UNEXPECTED_FAIL = 202
