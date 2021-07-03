import re
import enum


class UMT(enum.Enum):
    """
    Unix terminal format codes
    """
    NORMAL        = '\033[0m'
    BOLD          = '\033[1m'
    DIM           = '\033[2m'
    UNDERLINE     = '\033[4m'
    REVERSE       = '\033[7m'
    STRIKETHROUGH = '\033[9m'
    RED           = '\033[31m'
    YELLOW        = '\033[33m'


def fmt_currency(amount):
    """format as currency an string amount"""

    def makeup_intseg(int_seg):
        mut = []
        for idx , c in enumerate(reversed(int_seg)):
            mut.append(c)
            if ((idx + 1) % 3) == 0:
                mut.append(',')
        if mut[-1] == ',':
            del mut[-1]
        return ''.join(reversed(mut))

    m = re.match("^\d+(\.\d{1,2})?$", amount)
    if m:
        if amount.find(".") == -1:
             return "{0}.{1:0<2}".format(
                 makeup_intseg(amount), "0"
             )
        else:
             int_seg , decimal_seg = amount.split('.', 1)
             return "{0}.{1:0<2}".format(
                 makeup_intseg(int_seg), decimal_seg
             )
    else:
        raise Exception("input parameter is not an amount string")
