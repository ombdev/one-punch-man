from docmaker.gen import BuilderGen
from docmaker.error import DocBuilderImptError, DocBuilderStepError, DocBuilderError


def builder(self, resdir, rdirs_conf, bid, f_outdoc **kwargs):

    if resdir == None:
        raise DocBuilderError('resources directory not fed!!')

    if rdirs_conf == None:
        raise DocBuilderError("rdirs config info not fed!!")
