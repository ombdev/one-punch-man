import enum
from abc import ABCMeta, abstractmethod


class CfdiType(enum.Enum):
    """
    Cfdi types that shall be applied
    through cfdi writing customization
    """
    FAC = 0
    NCR = 1
    PAG = 2


class BuilderGen(metaclass=ABCMeta):
    """
    Builder interface base class.
    """

    def  __init__(self):
        pass

    def __str__(self):
        return self.__class__.__name__
