import yaml
import os
from engine.error import FatalError


def env_property(prop, caster=None):
    '''Read env variables for microservice's sake'''

    val = os.environ.get(prop)
    if val is None:
        raise FatalError("Enviroment variable {} has not been set !!".format(prop))

    if caster is None:
       return val

    try:
        return caster(val)
    except:
        raise FatalError("Enviroment variable {} could not be casted !!".format(prop))


def profile_read(p_file_path):
    """
    create a profile tree as per
    a determined config profile
    """

    def parse_profile():
        """
        Parses a profile in json format
        """

        try:
            stream = open(p_file_path)
            d = yaml.safe_load(stream)
            return d['profile']
        except (yaml.YAMLError, KeyError, OSError, IOError) as e:
            _logger.error(e)
            _logger.fatal("malformed profile file in: {0}".format(p_file_path))
            raise
        finally:
            stream.close()

    pt = parse_profile()
    pt['source'] = p_file_path
    return pt
