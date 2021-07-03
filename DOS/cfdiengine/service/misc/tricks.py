import sys
import traceback


def dump_exception():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(
        exc_type,
        exc_value,
        exc_traceback
    )
    return ''.join('!! ' + line for line in lines)
