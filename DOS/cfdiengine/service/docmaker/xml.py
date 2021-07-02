from decimal import Decimal
from docmaker.gen import BuilderGen, CfdiType


class FacXml(BuilderGen):

    _PROPOS = CfdiType.FAC

    def __init__(self):
        super().__init__()

    def data_acq(self, **kwargs):
        pass

    def format_wrt(self, dat, ofile):
        pass

    def data_rel(self, dat):
        pass
