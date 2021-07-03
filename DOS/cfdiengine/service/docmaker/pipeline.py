from docmaker.gen import BuilderGen
from docmaker.error import DocBuilderImptError, DocBuilderStepError, DocBuilderError

class DocPipeLine(object):
    """
    creator instance of documents.
    """

    def __init__(self, resdir = None, rdirs_conf = None):

        if resdir == None:
            raise DocBuilderError('resources directory not fed!!')
        if rdirs_conf == None:
            raise DocBuilderError("rdirs config info not fed!!")

        self.resdir, self.rdirs_conf = resdir, rdirs_conf
